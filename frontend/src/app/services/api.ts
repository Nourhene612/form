import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  // ───────────── INFORMATIONS GENERALES ─────────────
  getInformationsGenerales(): Observable<any> {
    return this.http.get(`${this.apiUrl}/informations-generales/`);
  }

  getInformationGeneraleById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/informations-generales/${id}`);
  }

  createInformationGenerale(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/informations-generales/`, data);
  }

  updateInformationGenerale(id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/informations-generales/${id}`, data);
  }

  deleteInformationGenerale(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/informations-generales/${id}`);
  }

  // ───────────── GESTION PROJET ─────────────
  getAllGestionProjet(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gestion-projet/`);
  }

  getGestionProjetById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/gestion-projet/${id}`);
  }

  getGestionProjetByInformationsId(informationsId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/gestion-projet/by-informations/${informationsId}`);
  }

  createGestionProjet(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/gestion-projet/`, data);
  }

  updateGestionProjet(id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/gestion-projet/${id}`, data);
  }

  deleteGestionProjet(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/gestion-projet/${id}`);
  }

  // ───────────── IMPACT ─────────────
  getImpactByInformationsId(informationsId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/impact/by-informations/${informationsId}`);
  }

  createImpact(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/impact/`, data);
  }

  updateImpact(informationsId: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/impact/by-informations/${informationsId}`, data);
  }

  deleteImpact(informationsId: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/impact/by-informations/${informationsId}`);
  }

  // ───────────── PERFORMANCE ─────────────
  getAllPerformance(): Observable<any> {
    return this.http.get(`${this.apiUrl}/performance/`);
  }

  getPerformanceById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/performance/${id}`);
  }

  createPerformance(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/performance/`, data);
  }

  updatePerformance(id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/performance/${id}`, data);
  }

  deletePerformance(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/performance/${id}`);
  }

  // ───────────── TESTS FONCTIONNELS ─────────────
  getTestFonctionnelById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/tests-fonctionnels/${id}`);
  }

  getTestFonctionnelByFormulaire(informationsId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/tests-fonctionnels/formulaire/${informationsId}`);
  }

  createTestFonctionnel(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/tests-fonctionnels/`, data);
  }

  updateTestFonctionnel(id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/tests-fonctionnels/${id}`, data);
  }

  patchTestFonctionnel(id: string, data: any): Observable<any> {
    return this.http.patch(`${this.apiUrl}/tests-fonctionnels/${id}`, data);
  }

  deleteTestFonctionnel(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/tests-fonctionnels/${id}`);
  }

  // ───────────── CICD ─────────────
  getAllCicd(): Observable<any> {
    return this.http.get(`${this.apiUrl}/cicd/`);
  }

  getCicdById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/cicd/${id}`);
  }

  getCicdByInformationsId(informationsId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/cicd/by-informations/${informationsId}`);
  }

  createCicd(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/cicd/`, data);
  }

  updateCicd(id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/cicd/${id}`, data);
  }

  deleteCicd(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/cicd/${id}`);
  }
}