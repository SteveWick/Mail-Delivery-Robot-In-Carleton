import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { RequestComponent } from './request/request.component';
import { FormsModule } from '@angular/forms';
import { RequestFormComponent } from './request-form/request-form.component';
import { MessagesComponent } from './messages/messages.component'
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    RequestComponent,
    RequestFormComponent,
    MessagesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
