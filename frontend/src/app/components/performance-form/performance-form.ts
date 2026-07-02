import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api';
import { SubmissionStateService } from '../../services/submission-state.service';

type FormMessageType = 'success' | 'error' | null;

interface CheckboxGroupConfig {
  name: string;
  autreName: string;
  errorMessage: string;
}

// ───────── Mapping valeurs formulaire → enums backend (Pydantic) ─────────

const DEGRADATION_PERFORMANCE_MAP: Record<string, string> = {
  jamais: 'Jamais',
  rarement: 'Rarement',
  oui: 'Oui, et cela a impacté nos ventes',
};

const TEST_CHARGE_REALISES_MAP: Record<string, string> = {
  toujours: 'Toujours', parfois: 'Parfois', jamais: 'Jamais',
};

const TYPE_TEST_CHARGE_MAP: Record<string, string> = {
  manuellement: 'Manuellement', automatises: 'Automatisés', les_deux: 'Les deux',
};

const ANOMALIES_PRODUCTION_MAP: Record<string, string> = {
  jamais: 'Jamais',
  rarement: 'Rarement',
  oui: 'Oui, avec un impact sur les utilisateurs / le business',
};

const TESTS_FONCTIONNELS_REALISES_MAP: Record<string, string> = {
  toujours: 'Toujours', parfois: 'Parfois', jamais: 'Jamais',
};

const TYPE_TEST_MAP: Record<string, string> = {
  manuellement: 'Manuellement', automatises: 'Automatisés', les_deux: 'Les deux',
};

const MOMENT_TEST_MAP: Record<string, string> = {
  shift_left: 'Dès la phase de développement (Shift-left)',
  avant_prod: 'Avant mise en production',
  apres_incident: 'Après incident en production',
};

const DISTRIBUTION_CHARGE_MAP: Record<string, string> = {
  oui: 'Oui', partiellement: 'Partiellement', non: 'Non',
};

const TYPE_METHODE_MAP: Record<string, string> = {
  agile: 'Agile (Scrum / Kanban)',
  v: 'Cycle en V (Waterfall)',
  hybride: 'Hybride',
  aucune: 'Pas de méthode définie',
};

const PROBLEME_RESSOURCES_MAP: Record<string, string> = {
  manque: 'Oui, manque de ressources (surcharge, lenteur)',
  surdimensionnement: 'Oui, surdimensionnement (coûts inutiles)',
  les_deux: 'Les deux',
  non: 'Non',
};

@Component({
  selector: 'app-performance-form',
  imports: [],
  templateUrl: './performance-form.html',
  styleUrl: './performance-form.scss',
})
export class PerformanceForm {

  formMessage = '';
  formMessageType: FormMessageType = null;
  isSubmitting = false;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private submissionState: SubmissionStateService,
  ) {}

  private checkboxGroups: CheckboxGroupConfig[] = [
    { name: 'outils_gestion_proj', autreName: 'outils_gestion_proj_autre', errorMessage: 'Sélectionnez au moins un outil de gestion de projet ou précisez-en un autre.' },
    { name: 'aspects_couverts', autreName: 'aspects_couverts_autre', errorMessage: 'Sélectionnez au moins un aspect couvert ou précisez-en un autre.' },
    { name: 'integrations', autreName: 'integrations_autre', errorMessage: 'Sélectionnez au moins une intégration ou précisez-en une autre.' },
    { name: 'rework_causes', autreName: 'rework_causes_autre', errorMessage: 'Sélectionnez au moins une cause de rework ou précisez-en une autre.' },
  ];

  onSubmit(event?: Event) {
    event?.preventDefault();

    if (this.isSubmitting) {
      return;
    }

    const form = document.querySelector('form') as HTMLFormElement;
    if (!form) return;

    for (const group of this.checkboxGroups) {
      if (!this.isCheckboxGroupValid(group.name, group.autreName)) {
        this.showMessage(group.errorMessage, 'error');
        return;
      }
    }

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    this.isSubmitting = true;
    const fd = new FormData(form);

    // ───────── INFORMATIONS GENERALES ─────────
    const informationsPayload = {
      dateEvaluation: new Date().toISOString().split('T')[0],
      nom: this.get(fd, 'nom'),
      prenom: this.get(fd, 'prenom'),
      email: this.get(fd, 'email'),
      mobile: this.get(fd, 'mobile') || null,
      entreprise: this.get(fd, 'entreprise') || null,
      secteurActivite: this.get(fd, 'secteur') || null,
    };

    this.apiService.createInformationGenerale(informationsPayload).subscribe({
      next: (response) => {
        const informationsId = response.idEvaluation;
        this.submitSousFormulaires(fd, informationsId, form);
      },
      error: (err) => {
        console.error(err);
        this.isSubmitting = false;
        this.showMessage("Erreur lors de l'envoi des informations générales.", 'error');
      }
    });
  }

  private submitSousFormulaires(fd: FormData, informationsId: string, form: HTMLFormElement) {
    // ───────── PERFORMANCE ─────────
    const performancePayload = {
      degradationPerformance: DEGRADATION_PERFORMANCE_MAP[this.get(fd, 'degradations_trafic')] ?? null,
      impactVentes: this.get(fd, 'degradations_trafic') === 'oui',
      testsChargeRealises: TEST_CHARGE_REALISES_MAP[this.get(fd, 'tests_charge')] ?? null,
      typeTestCharge: TYPE_TEST_CHARGE_MAP[this.get(fd, 'methode_charge')] ?? null,
      informations_id: informationsId,
      outils: this.toNomList(fd, 'outils_charge', 'outils_charge_autre'),
    };

    // ───────── TESTS FONCTIONNELS ─────────
    const testFonctionnelPayload = {
      anomaliesProduction: ANOMALIES_PRODUCTION_MAP[this.get(fd, 'anomalies_prod')] ?? null,
      testsFonctionnelsRealises: TESTS_FONCTIONNELS_REALISES_MAP[this.get(fd, 'tests_fonctionnels')] ?? null,
      typeTest: TYPE_TEST_MAP[this.get(fd, 'methode_fonctionnels')] ?? null,
      informations_id: informationsId,
      outils: this.toNomList(fd, 'outils_fonc', 'outils_fonc_autre'),
    };

    
    const cicdPayload = {
      utiliseCICD: this.get(fd, 'cicd_use') === 'oui',
      outil: this.toJoinedString(fd, 'outils_cicd', 'outils_cicd_autre') || null,
      testPerformanceIntegre: this.get(fd, 'perf_inc_cicd') === 'oui',
      momentTest: MOMENT_TEST_MAP[this.get(fd, 'timing_tests')] ?? null,
      distributionCharge: DISTRIBUTION_CHARGE_MAP[this.get(fd, 'charge_reelle')] ?? null,
      informations_id: informationsId,
    };

    
    const gestionProjetPayload = {
      typeMethode: TYPE_METHODE_MAP[this.get(fd, 'methodo_projet')] ?? null,
      outil_gestion: this.get(fd, 'outil_gestion') || null,
      aspects_couverts: this.getAll(fd, 'aspects_couverts'),
      informations_id: informationsId,
      outils: this.toNomList(fd, 'outils_gestion_proj', 'outils_gestion_proj_autre'),
      integrations: this.toTypeIntegrationList(fd, 'integrations', 'integrations_autre'),
    };

    
    const impactPayload = {
      nombreRessources: this.toInt(this.get(fd, 'ressources_fte')),
      coutIncident: this.parseMontant(this.get(fd, 'cout_incident')),
      tempsResolution: this.get(fd, 'temps_resolution') || null,
      causesRework: this.toJoinedString(fd, 'rework_causes', 'rework_causes_autre') || null,
      problemeRessources: PROBLEME_RESSOURCES_MAP[this.get(fd, 'probleme_ressources')] ?? null,
      informations_id: informationsId,
    };

    Promise.all([
      this.apiService.createPerformance(performancePayload).toPromise(),
      this.apiService.createTestFonctionnel(testFonctionnelPayload).toPromise(),
      this.apiService.createCicd(cicdPayload).toPromise(),
      this.apiService.createGestionProjet(gestionProjetPayload).toPromise(),
      this.apiService.createImpact(impactPayload).toPromise(),
    ])
      .then(() => {
        this.isSubmitting = false;
        const submissionData = {
          companyName: this.get(fd, 'entreprise'),
          contactName: `${this.get(fd, 'prenom')} ${this.get(fd, 'nom')}`,
          email: this.get(fd, 'email'),
          phone: this.get(fd, 'mobile'),
          sector: this.get(fd, 'secteur'),
          submissionDate: new Date().toISOString(),
          submissionId: informationsId,
          additionalInfo: {
            tools: this.getAll(fd, 'outils_charge').concat(this.getAll(fd, 'outils_fonc')),
            comments: this.get(fd, 'temps_resolution') || null,
          },
        };

        this.submissionState.setSubmissionData(submissionData);
        this.router.navigate(['/confirmation'], { state: { submissionData } });
      })
      .catch((err) => {
        console.error(err);
        this.isSubmitting = false;
        this.showMessage("Erreur lors de l'envoi d'une des sections du formulaire.", 'error');
      });
  }

  // ───────────── Helpers ─────────────

  private get(fd: FormData, name: string): string {
    return (fd.get(name) as string)?.trim() ?? '';
  }

  private getAll(fd: FormData, name: string): string[] {
    return fd.getAll(name).map(v => v as string).filter(v => v !== '');
  }

  private toNomList(fd: FormData, checkboxName: string, autreName: string): { nom: string }[] {
    const values = this.getAll(fd, checkboxName);
    const autre = this.get(fd, autreName);
    if (autre) values.push(autre);
    return values.map(v => ({ nom: v }));
  }

  private toTypeIntegrationList(fd: FormData, checkboxName: string, autreName: string): { typeIntegration: string }[] {
    const values = this.getAll(fd, checkboxName);
    const autre = this.get(fd, autreName);
    if (autre) values.push(autre);
    return values.map(v => ({ typeIntegration: v }));
  }

  private toJoinedString(fd: FormData, checkboxName: string, autreName: string): string {
    const values = this.getAll(fd, checkboxName);
    const autre = this.get(fd, autreName);
    if (autre) values.push(autre);
    return values.join(', ');
  }

  private toInt(value: string): number | null {
    const n = parseInt(value, 10);
    return isNaN(n) ? null : n;
  }

  private parseMontant(value: string): number | null {
    const match = value.replace(',', '.').match(/[\d.]+/);
    return match ? parseFloat(match[0]) : null;
  }

  onCancel() {
    const form = document.querySelector('form') as HTMLFormElement;
    form?.reset();
    this.showMessage('Le formulaire a été réinitialisé', 'success');
  }

  private isCheckboxGroupValid(name: string, autreName: string): boolean {
    const checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
    const autreInput = document.querySelector(`input[name="${autreName}"]`) as HTMLInputElement | null;
    const autre = autreInput ? autreInput.value.trim() : '';
    return checkboxes.length > 0 || autre !== '';
  }

  private showMessage(message: string, type: FormMessageType) {
    this.formMessage = message;
    this.formMessageType = type;
    setTimeout(() => {
      this.formMessage = '';
      this.formMessageType = null;
    }, 5000);
  }
}