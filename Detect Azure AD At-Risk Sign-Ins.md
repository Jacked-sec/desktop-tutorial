title: Detect Azure AD At-Risk Sign-Ins
id: 12345678-1234-1234-1234-123456789abc
status: experimental
description: Detects Azure Active Directory sign-ins marked as "atRisk" with associated details.
author: Your Name
date: 2024-11-25
logsource:
  product: azure
  service: aad_signin
detection:
  selection:
    properties_riskState: "atRisk"
  group_by:
    - customerDomain
    - properties_ipAddress
    - properties_signInIdentifier
    - properties_status_failureReason
    - properties_resourceDisplayName
    - riskEventTypes
  timeframe: 30m
  condition: selection
fields:
  - timestamp
  - properties_location_city
  - properties_location_state
  - properties_location_countryOrRegion
  - properties_userAgent
  - properties_riskLevelAggregated
  - properties_userDisplayName
  - properties_userPrincipalName
  - properties_deviceDetail_browser
output:
  count:
    type: count
    timeframe: 5m
falsepositives:
  - Unusual but legitimate logins
level: medium
