Feature: Check working
Scenario: Сheck work site
  Given website "http://127.0.0.1:8000/"
  When push button with div 'fs_start_game'
  Then page include div 'rounds-container'