import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SubmissionStateService {
  private readonly submissionDataSignal = signal<any | null>(null);

  setSubmissionData(data: any): void {
    this.submissionDataSignal.set(data);
  }

  getSubmissionData() {
    return this.submissionDataSignal;
  }
}