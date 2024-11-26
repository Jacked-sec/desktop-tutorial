# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.
title: Detect Azure AD Sign-In login Fail 
description: Detects Azure AD sign-ins login fail 10 time in 1h min with specific error codes and aggregates data for analysis.
author: Jacked
date: 2024-11-25
logsource:
  product: azure
  service: aad_signin
detection:
  selection:
    category: "SignInLogs"
    properties_status_errorCode:
      - "50126"
      - "50055"
      - "50057"
  aggregation:
    timeframe: 1h
    group_by:
      - properties_userPrincipalName
      - category
      - customerDomain
    condition: count() > 10
  condition: selection and aggregation
fields:
  - properties_userPrincipalName
  - properties_userDisplayName
  - properties_status_errorCode
  - properties_status_failureReason
  - properties_ipAddress
  - properties_appDisplayName
  - ip4
  - ISPip4
  - ip6
  - ISPip6
  - src_ip
falsepositives:
  - Unusual but legitimate login issues
level: medium
references:
  - https://docs.microsoft.com/en-us/azure/active-directory/
