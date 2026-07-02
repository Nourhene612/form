import { Routes } from '@angular/router';
import { PerformanceForm } from './components/performance-form/performance-form';
import { Success } from './components/success/success';

export const routes: Routes = [
	{ path: '', component: PerformanceForm },
	{ path: 'confirmation', component: Success },
	{ path: '**', redirectTo: '' },
];
