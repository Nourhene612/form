import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink } from '@angular/router';
import { SubmissionStateService } from '../../services/submission-state.service';

@Component({
  selector: 'app-success',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './success.html',
  styleUrl: './success.scss',
})
export class Success implements OnInit {

  submissionData: any = null;

  constructor(
    private router: Router,
    private submissionState: SubmissionStateService,
  ) {}

  ngOnInit(): void {
    // Priorité au state de navigation, puis au store partagé du client.
    this.submissionData = history.state?.submissionData ?? this.submissionState.getSubmissionData()();

    if (!this.submissionData) {
      console.warn('Aucune donnée de soumission trouvée. Accès direct ou rechargement de la page.');
      // Optionnel : rediriger si personne n'arrive avec des données valides
      // this.router.navigate(['/']);
    }
  }

  print(): void {
    window.print();
  }
}