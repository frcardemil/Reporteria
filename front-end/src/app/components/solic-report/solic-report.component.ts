import { Component, NgModule } from '@angular/core';

@Component({

  selector: 'app-solic-report',
  standalone: true,
  imports: [],
  templateUrl: './solic-report.component.html',
  styleUrl: './solic-report.component.css'
})

export class SolicReportComponent {
  cantFiles:number = 1;
  constructor (){}
}
