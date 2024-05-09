import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolicReportComponent } from './solic-report.component';

describe('SolicReportComponent', () => {
  let component: SolicReportComponent;
  let fixture: ComponentFixture<SolicReportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SolicReportComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SolicReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
