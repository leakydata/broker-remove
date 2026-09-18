# Imprint Analytics LLC

- **Email:** privacy@imprintanalytics.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** imprintanalytics.io
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: HARD BOUNCE 2026-08-28: privacy@imprintanalytics.io -> 550 5.1.1 'the email account that you tried to reach does not exist'. That address is the one Imprint Analytics LLC FILED ON THE CALIFORNIA DATA BROKER REGISTRY, and it is the only contact the company publishes anywhere: imprintanalytics.io has live Google Workspace MX but serves no website (TLS handshake fails outright; plain HTTP returns Cloudflare error 1001), so discover_contacts found nothing and there is no privacy policy page to read a second address off. A registered broker with a mailbox that does not exist and no site is unreachable by every route the statute creates. Handoff: CA AG complaint is the remaining lever.

## Steps

There is no route. Recorded so nobody spends a send rediscovering that.

    dig +short MX imprintanalytics.io   -> aspmx.l.google.com. and friends (live)
    dig +short A  imprintanalytics.io   -> 160.153.0.60 (GoDaddy parking range)
    curl -I https://imprintanalytics.io -> exit 35, TLS handshake fails
    curl -I http://imprintanalytics.io  -> HTTP 409, body "error code: 1001"

Both DNS checks pass. The mail check passes. The domain resolves and answers on
port 80. Every cheap signal this project uses to decide a broker is alive says
yes, and there is still no company on the other end -- no page, no privacy
policy, no second address. See `_SILENT_FAILURES.md` §145.

## Gotchas

**Do not stop at DNS-health checks.** MX resolves, the A record resolves, port
80 answers — every check this project normally runs to decide a domain is
alive says yes, and there is still no reachable company behind any of them.
See `_SILENT_FAILURES.md` §145.

## Verification

Nothing to verify — no route exists (see Status/Steps above). Re-check
periodically whether imprintanalytics.io starts serving a real site.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Imprint Analytics LLC
- **Registered address:** 9499 Collins Avenue, # 509, Surfside, CA 33154,
  United States
- **Filed contact email:** privacy@imprintanalytics.io
- **Website:** http://www.imprintanalytics.io
- **Opt-out route they filed:** Right to Opt Out of Sale:, , All USA
  residents have the right to opt out of the sale of their Personal
  Information. All USA residents may submit these requests via this
  webform or via email to privacy@imprintanalytics.io. If you email us,
  then please attach the by sending the Personal Information Request form
  (see below) to the email. , , Right to Know:, All USA residents have
  the right to know what Personal Information we collect, use, disclose
  and/or sell about you. California residents may submit these requests
  via email to privacy@imprintanalytics.io, via this webform, or by
  calling the toll-free number (888)-794-6774. If you email us, then
  please attach the by sending the Personal Information Request form (see
  below) to the email. For more information about how we process these
  requests, see Submitting Requests section below. , Right to Deletion:,
  Certain USA Statesâ€™ residents have the right to request deletion of
  their Personal Information collected by us. Imprint Analytics LLC
  extends these rights to all residents of the USA. If you email us, then
  please attach the by sending the Personal Information Request form (see
  below) to the email privacy@imprintanalytics.io. For more information
  about how we process these requests, see Submitting Requests section
  below. , Right to Non-Discrimination for the Exercise of Privacy
  Rights:, All USA residents have the right not to receive discriminatory
  treatment for exercising any of the privacy rights conferred by the
  CCPA, except as permitted under the CCPA. If you believe you have
  received discriminatory treatment by Imprint Analytics LLC for
  exercising your CCPA privacy rights, please contact us as set forth
  below., You can exercise these rights yourself or you can designate an
  authorized agent to make a request on your behalf. Your authorized
  agent must be able to demonstrate authority to act on your behalf as
  further instructed when submitting a verifiable request on your
  behalf., Your Rights , All visitors or users of this website have the
  following rights with regard to their personal information:, The right
  to access your information., The right to know whether your personal
  information is sold or disclosed and to whom., The right to say no to
  the sale of your personal information., The right to request that we
  delete all or some of the personal information that we have collected
  on you., The right to equal service and price, even if you exercise
  your privacy rights., , Right to Opt Out of Sale:, , All USA residents
  have the right to opt out of the sale of their Personal Information.
  All USA residents may submit these requests via this webform, or via
  email to privacy@imprintanalytics.io. If you email us, then please
  attach the by sending the Personal Information Request form (see below)
  to the email. , , Right to Know:, All USA residents have the right to
  know what Personal Information we collect, use, disclose and/or sell
  about you. California residents may submit these requests via email to
  privacy@imprintanalytics.io, via this webform, or by calling the
  toll-free number (888)-794-6774. If you email us, then please attach
  the by sending the Personal Information Request form (see below) to the
  email. For more information about how we process these requests, see
  Submitting Requests section below. , Right to Deletion:, Certain USA
  Statesâ€™ residents have the right to request deletion of their
  Personal Information collected by us. Imprint Analytics LLC extends
  these rights to all residents of the USA. If you email us, then please
  attach the by sending the Personal Information Request form (see below)
  to the email privacy@imprintanalytics.io. For more information about
  how we process these requests, see Submitting Requests section below. ,
  Right to Non-Discrimination for the Exercise of Privacy Rights:, All
  USA residents have the right not to receive discriminatory treatment
  for exercising any of the privacy rights conferred by the CCPA, except
  as permitted under the CCPA. If you believe you have received
  discriminatory treatment by Imprint Analytics LLC for exercising your
  CCPA privacy rights, please contact us as set forth below., You can
  exercise these rights yourself or you can designate an authorized agent
  to make a request on your behalf. Your authorized agent must be able to
  demonstrate authority to act on your behalf as further instructed when
  submitting a verifiable request on your behalf., Your Rights , All
  visitors or users of this website have the following rights with regard
  to their personal information:, , The right to access your information
  , The right to know whether your personal information is sold or
  disclosed and to whom., The right to say no to the sale of your
  personal information., The right to request that we delete all or some
  of the personal information that we have collected on you., The right
  to equal service and price, even if you exercise your privacy rights.,
  Exercising your rights, You may exercise the rights specified above by
  submitting a consumer request to:, privacy@imprintanalytics.io,
  (888)-794-6774, www.imprintanalytics.io/privacy, Imprint Analytics LLC,
  9499 Collins Ave, # 509 Surfside, FL 33154 United States, , , We will
  need to verify your identity prior to effectuating your request. To
  verify your identity, you will need to provide us with the following
  information with your request:, Name;, Postal / Shipping address;,
  Phone number;, Email address., Please note that we may be unable to
  process your request if you do not provide us with the above
  information., You may also designate an authorized agent to exercise
  your rights on your behalf. You may designate an agent via any of the
  ways used to submit requests on your behalf. We will request the agent
  to verify that he or she has the authority to submit requests on your
  behalf. We will do so by asking the agent to submit the following
  information:, Valid power of attorney;, consumerâ€™s signed permission
  demonstrating that you have been authorized by the consumer to act on
  the consumerâ€™s behalf., Please note that we may not be able to
  process your request if your designated agent and/or you do not provide
  us with the above information., We will respond to most consumer
  requests within 30 to 45 days of receipt, depending upon where you
  reside. However, some requests may take longer. We will notify you in
  writing if we need more time to respond. We have the ability to deny
  your request(s) if certain exceptions in the law apply. If we do deny
  your request, we will provide you with the reasons for such denial.,
  You have the right to appeal a refusal to take action on a rights
  request. You may file an appeal to us at the contact information
  provided above. We will respond to most appeal requests within 45 days
  of receipt. However, some requests may take longer. We will notify you
  in writing if we need more time to respond (up to 90 days total). In
  our response to your appeal, we will inform you of any actions taken or
  not taken and the reason(s) as to why. Normally, we do not charge a fee
  to process or respond to consumer requests. However, we may charge a
  fee for a second or subsequent request within a 12-month period., , ,
  â€”----------------------------------------------------------------------------------------------------------------------------------
  , Personal Information Request Form: , If you would like to submit to
  Imprint Analytics LLC a request related to your personal information,
  please provide the information below so Imprint Analytics LLC can
  respond appropriately. Imprint Analytics LLC may need additional
  information from you to verify your identity, to assess the relevant
  legal requirements, or generally to process your request., If you would
  like to unsubscribe from Imprint Analytics LLC marketing
  communications, do not submit this form. Instead, please update your
  marketing preferences by clicking on the "Unsubscribe" link at the
  bottom of the email you received, or alternatively, by emailing
  privacy@imprintanalytics.io if the â€œUnsubscribeâ€ option in the
  email is not available. , First Name: , Last Name:, Aliases or former
  names: , If you are an Imprint Analytics LLC partner or supplier, name
  of the company: , , , Email address: , *Please provide any email
  addresses for you that you believe we may possess , Phone Number:,
  *Please provide any phone number for you that you believe we may
  possess. , Postal Address:, *Include your street address, city,
  state/province, and zip/postal code. , I am a: â–¡ Enterprise Customer;
  â–¡ Consumer/Marketing Recipient; â–¡ Current Employee/Contractor; â–¡
  Former Employee/Contractor; â–¡ Job Applicant. , Get a copy of your
  data: , â–¡ See a report that shows the personal data weâ€™ve shared,
  and the types of companies weâ€™ve shared it with. , Type of request:
  Other (Specify Below):, *Additional Details, , We will use the
  information you provide in this form to respond to your request. , , By
  submitting this form, I confirm that: , â–¡ The above information is
  true and correct, and I am the person, or the parent, guardian, or, an
  authorized agent of the individual identified above. If an authorized
  agent, I may be required to provide additional documentation as
  indicated by Imprint Analytics LLC or as set forth on our Privacy
  Policy., , â–¡ I understand that my request will be processed in
  accordance with applicable law and that certain exceptions and
  exclusions may apply to the handling of my request., , , â–¡ I
  understand that if I request BIGDBM to delete my information, such
  deletion is irreversible, and the information will be unrecoverable., ,
  , Signature: , , Print Name:, , Date:, , Instructions: complete, sign,
  and scan this form and email it to privacy@imprintanalytics.io or mail
  it to: , Imprint Analytics, Attn: Privacy, 9499 Collins Ave, #509,
  Surfside FL 33154,
  â€”----------------------------------------------------------------------------------------------------------------------------------,
  Submitting Requests:, When you submit your Right to Opt Out of Sale
  request, we will ask you to provide your name and contact information
  so that we can communicate with you regarding your request and process
  your request. , When you submit your Right to Know request or Right to
  Delete request, we will ask you to provide your name and contact
  information so that we can communicate with you regarding your request
  and process your request. , In addition, for your privacy and security
  and to prevent fraud or other harmful activities, when we receive a
  Right to Know request or a Right to Delete request, we may ask for
  information that we will use to verify your identity. For requests of
  specific pieces of personal information about a consumer, we will
  verify your identity to a reasonably high degree of certainty; whereas
  for requests to know categories of information or for requests to
  delete we will verify your identity to a reasonable degree of
  certainty. Providing accurate information that matches our records is
  necessary so that we can locate the correct information within our
  systems and among our service providers. The information we may ask you
  to provide includes your name, mailing address and either your mobile
  phone number or your email address. , Do not send us, directly or
  indirectly, any sensitive or special categories of Personal Information
  (e.g., social security numbers or other national or state identifiers,
  health information, biometric data or genetic characteristics, criminal
  background information, financial account numbers, payment card
  information, and so on) on or through the Website or otherwise. , We
  will evaluate and respond to your request to the extent required by law
  (or in our discretion if not required by law) and as permitted by our
  contracts, confidentiality obligations, and applicable laws and
  regulations. We may not be able to provide all of the information
  requested due to certain exceptions enumerated in tother applicable
  laws. If we do not have sufficient information about you to verify your
  identity, we may not be able to identify you and will be unable to
  process your request. We will attempt to verify your identity by using
  the information you submit with your request matching it with the
  information we possess about you. We may need to request additional
  information to sufficiently identify you., If you are an authorized
  agent submitting a request on behalf of a consumer, please also email
  the below information to privacy@imprintanalytics.io or attach the
  appropriate documentation to this webform., Authorized Agents, If you
  are an authorized agent operating as a business, then together with the
  consumer request, please provide the following:, Evidence that your
  business is registered to conduct business in the State of California
  or other applicable State;, A written authorization document signed and
  dated by each consumer authorizing the business as the authorized agent
  to act on behalf of each consumer in making the request;, Valid email
  address or other contact information for each consumer for our direct
  correspondence with each consumer, including as deemed necessary or
  legally required completion of an identity verification process., If
  you are an individual and acting as an authorized agent on behalf of a
  consumer, then together with the consumer request please provide:, A
  â€œpower of attorneyâ€ pursuant to California Probate Code Sections
  4121 â€“ 4130; or other USA State,, If no power of attorney is
  available, then provide:, A written authorization document signed by
  the consumer authorizing the agent to act as the authorized agent on
  behalf of the consumer; and, Valid email address or other contact
  information for each consumer for our direct correspondence with each
  consumer, including as deemed necessary or legally required completion
  of an identity verification process., â€œShine the Lightâ€ Law , In
  accordance with the California Shine the Light law, California
  residents may request certain information regarding our disclosure (if
  any) of Personal Information to third parties for their direct
  marketing purposes. Other than to third party recipients as set forth
  in this Privacy Policy (Section 4, How We Share Your Personal
  Information), or unless you request us to or consent to it, we do not
  share your Personal Information with third parties for their own direct
  marketing purposes. For any questions on these practices, please
  contact us at privacy@imprintanalytics.io., Location of Data
  Processing, All data processing activities undertaken by us take place
  in the United States., Other Important Information, Data Accuracy,
  Imprint Analytics LLC maintains quality control procedures to ensure
  the Personal Information we store is as accurate and complete as
  reasonably possible. We have developed proprietary technology to
  constantly evaluate the accuracy of the Personal Information we store,
  identify inaccurate Personal Information, and update the Personal
  Information as applicable and as reasonably practicable., Links to
  Third Party Sites, The Website may contain links to unaffiliated
  third-party sites. Imprint Analytics LLC and its affiliate sites do not
  endorse or make any representations about any third-party sites
  including any information found on such sites. We encourage you to
  review the privacy policies and terms of use of these unaffiliated
  third-party sites., Security , Imprint Analytics LLC maintains
  organizational, technical and physical security procedures, including
  those required by applicable laws, designed to protect Personal
  Information we store from accidental or unlawful destruction or
  accidental loss, damage, alteration, unauthorized disclosure or access,
  as well as all other forms of unlawful processing. Measures are taken
  to prevent unauthorized access, alteration, or dissemination of
  personal information. We also maintain physical security for our
  facilities and limit access to certain critical areas of our business.
  However, security risk is inherent in all internet and information
  technologies, and we cannot guarantee the security of your Personal
  Information., If we learn of and confirm the occurrence of a security
  incident leading to the misappropriation or accidental or unlawful
  destruction, loss, alteration, unauthorized disclosure of, or access
  to, your Personal Information transmitted, stored or otherwise
  processed on our systems that compromises the confidentiality,
  integrity or availability of your Personal Information, we may attempt
  to notify you electronically by posting a notice on the Website or by
  sending you an email or otherwise in accordance with applicable law.,
  Changes to This Policy, Imprint Analytics LLC may revise this Privacy
  Policy from time to time. We reserve the right to amend this Privacy
  Policy at any time. Any changes to this Privacy Policy will be posted
  here or other successor locations available from this page. You can
  determine when this Privacy Policy was last revised by checking the
  â€œLast Revisedâ€ legend at the bottom of this Privacy Policy., Filing
  a Complaint, If you have any complaints regarding our compliance with
  this Privacy Policy, please contact us. We will investigate and attempt
  to resolve complaints and disputes regarding use and disclosure of
  personal information in accordance with this Privacy Policy and in
  accordance with applicable law. You also have the right to file a
  complaint with a competent data protection authority., Information on
  the consumer requests that we have received, Below is additional
  information on the requests to exercise privacy rights that we have
  received from California consumers:, We have received 0 requests to
  know. We complied in whole or in part with N/A and denied N/A of these
  requests., We have received 0 requests to delete. We complied in whole
  or in part with N/A and denied N/A of these requests., We have received
  0 requests to opt out. We complied in whole or in part with N/A and
  denied N/A of these requests., The median number of days within which
  we have substantively responded to these requests is N/A., Data
  Protection Officer, Charles Harriman is our Data Protection Officer and
  may be reached via email at: [named individual]@imprintanalytics.io,
  Third-party websites, This Website may contain hyperlinks to websites
  operated by parties other than us. We provide such hyperlinks for your
  reference only. We do not control such websites and are not responsible
  for their contents or the privacy or other practices of such websites.
  It is up to you to read and fully understand their Privacy Policies.
  Our inclusion of hyperlinks to such websites does not imply any
  endorsement of the material on such websites or any association with
  their operators., Do Not Track, Do Not Track is a preference you can
  set on your browser to inform websites that you do not want to be
  tracked. We do not support Do Not Track ("DNT"). You can either enable
  or disable Do Not Track by visiting the Preferences or Settings page of
  your browser., Transferring data, We plan to transfer data to the
  United States., Questions, If you have any questions about this Privacy
  Policy, please contact us at privacy@imprintanalytics.io., , ,
- **Route for protected individuals:** Right to Opt Out of Sale:, , All
  USA residents have the right to opt out of the sale of their Personal
  Information. All USA residents may submit these requests via this
  webform or via email to privacy@imprintanalytics.io. If you email us,
  then please attach the by sending the Personal Information Request form
  (see below) to the email. , , Right to Know:, All USA residents have
  the right to know what Personal Information we collect, use, disclose
  and/or sell about you. California residents may submit these requests
  via email to privacy@imprintanalytics.io, via this webform, or by
  calling the toll-free number (888)-794-6774. If you email us, then
  please attach the by sending the Personal Information Request form (see
  below) to the email. For more information about how we process these
  requests, see Submitting Requests section below. , Right to Deletion:,
  Certain USA Statesâ€™ residents have the right to request deletion of
  their Personal Information collected by us. Imprint Analytics LLC
  extends these rights to all residents of the USA. If you email us, then
  please attach the by sending the Personal Information Request form (see
  below) to the email privacy@imprintanalytics.io. For more information
  about how we process these requests, see Submitting Requests section
  below. , Right to Non-Discrimination for the Exercise of Privacy
  Rights:, All USA residents have the right not to receive discriminatory
  treatment for exercising any of the privacy rights conferred by the
  CCPA, except as permitted under the CCPA. If you believe you have
  received discriminatory treatment by Imprint Analytics LLC for
  exercising your CCPA privacy rights, please contact us as set forth
  below., You can exercise these rights yourself or you can designate an
  authorized agent to make a request on your behalf. Your authorized
  agent must be able to demonstrate authority to act on your behalf as
  further instructed when submitting a verifiable request on your
  behalf., Your Rights , All visitors or users of this website have the
  following rights with regard to their personal information:, The right
  to access your information., The right to know whether your personal
  information is sold or disclosed and to whom., The right to say no to
  the sale of your personal information., The right to request that we
  delete all or some of the personal information that we have collected
  on you., The right to equal service and price, even if you exercise
  your privacy rights., , Right to Opt Out of Sale:, , All USA residents
  have the right to opt out of the sale of their Personal Information.
  All USA residents may submit these requests via this webform, or via
  email to privacy@imprintanalytics.io. If you email us, then please
  attach the by sending the Personal Information Request form (see below)
  to the email. , , Right to Know:, All USA residents have the right to
  know what Personal Information we collect, use, disclose and/or sell
  about you. California residents may submit these requests via email to
  privacy@imprintanalytics.io, via this webform, or by calling the
  toll-free number (888)-794-6774. If you email us, then please attach
  the by sending the Personal Information Request form (see below) to the
  email. For more information about how we process these requests, see
  Submitting Requests section below. , Right to Deletion:, Certain USA
  Statesâ€™ residents have the right to request deletion of their
  Personal Information collected by us. Imprint Analytics LLC extends
  these rights to all residents of the USA. If you email us, then please
  attach the by sending the Personal Information Request form (see below)
  to the email privacy@imprintanalytics.io. For more information about
  how we process these requests, see Submitting Requests section below. ,
  Right to Non-Discrimination for the Exercise of Privacy Rights:, All
  USA residents have the right not to receive discriminatory treatment
  for exercising any of the privacy rights conferred by the CCPA, except
  as permitted under the CCPA. If you believe you have received
  discriminatory treatment by Imprint Analytics LLC for exercising your
  CCPA privacy rights, please contact us as set forth below., You can
  exercise these rights yourself or you can designate an authorized agent
  to make a request on your behalf. Your authorized agent must be able to
  demonstrate authority to act on your behalf as further instructed when
  submitting a verifiable request on your behalf., Your Rights , All
  visitors or users of this website have the following rights with regard
  to their personal information:, , The right to access your information
  , The right to know whether your personal information is sold or
  disclosed and to whom., The right to say no to the sale of your
  personal information., The right to request that we delete all or some
  of the personal information that we have collected on you., The right
  to equal service and price, even if you exercise your privacy rights.,
  Exercising your rights, You may exercise the rights specified above by
  submitting a consumer request to:, privacy@imprintanalytics.io,
  (888)-794-6774, www.imprintanalytics.io/privacy, Imprint Analytics LLC,
  9499 Collins Ave, # 509 Surfside, FL 33154 United States, , , We will
  need to verify your identity prior to effectuating your request. To
  verify your identity, you will need to provide us with the following
  information with your request:, Name;, Postal / Shipping address;,
  Phone number;, Email address., Please note that we may be unable to
  process your request if you do not provide us with the above
  information., You may also designate an authorized agent to exercise
  your rights on your behalf. You may designate an agent via any of the
  ways used to submit requests on your behalf. We will request the agent
  to verify that he or she has the authority to submit requests on your
  behalf. We will do so by asking the agent to submit the following
  information:, Valid power of attorney;, consumerâ€™s signed permission
  demonstrating that you have been authorized by the consumer to act on
  the consumerâ€™s behalf., Please note that we may not be able to
  process your request if your designated agent and/or you do not provide
  us with the above information., We will respond to most consumer
  requests within 30 to 45 days of receipt, depending upon where you
  reside. However, some requests may take longer. We will notify you in
  writing if we need more time to respond. We have the ability to deny
  your request(s) if certain exceptions in the law apply. If we do deny
  your request, we will provide you with the reasons for such denial.,
  You have the right to appeal a refusal to take action on a rights
  request. You may file an appeal to us at the contact information
  provided above. We will respond to most appeal requests within 45 days
  of receipt. However, some requests may take longer. We will notify you
  in writing if we need more time to respond (up to 90 days total). In
  our response to your appeal, we will inform you of any actions taken or
  not taken and the reason(s) as to why. Normally, we do not charge a fee
  to process or respond to consumer requests. However, we may charge a
  fee for a second or subsequent request within a 12-month period., , ,
  â€”----------------------------------------------------------------------------------------------------------------------------------
  , Personal Information Request Form: , If you would like to submit to
  Imprint Analytics LLC a request related to your personal information,
  please provide the information below so Imprint Analytics LLC can
  respond appropriately. Imprint Analytics LLC may need additional
  information from you to verify your identity, to assess the relevant
  legal requirements, or generally to process your request., If you would
  like to unsubscribe from Imprint Analytics LLC marketing
  communications, do not submit this form. Instead, please update your
  marketing preferences by clicking on the "Unsubscribe" link at the
  bottom of the email you received, or alternatively, by emailing
  privacy@imprintanalytics.io if the â€œUnsubscribeâ€ option in the
  email is not available. , First Name: , Last Name:, Aliases or former
  names: , If you are an Imprint Analytics LLC partner or supplier, name
  of the company: , , , Email address: , *Please provide any email
  addresses for you that you believe we may possess , Phone Number:,
  *Please provide any phone number for you that you believe we may
  possess. , Postal Address:, *Include your street address, city,
  state/province, and zip/postal code. , I am a: â–¡ Enterprise Customer;
  â–¡ Consumer/Marketing Recipient; â–¡ Current Employee/Contractor; â–¡
  Former Employee/Contractor; â–¡ Job Applicant. , Get a copy of your
  data: , â–¡ See a report that shows the personal data weâ€™ve shared,
  and the types of companies weâ€™ve shared it with. , Type of request:
  Other (Specify Below):, *Additional Details, , We will use the
  information you provide in this form to respond to your request. , , By
  submitting this form, I confirm that: , â–¡ The above information is
  true and correct, and I am the person, or the parent, guardian, or, an
  authorized agent of the individual identified above. If an authorized
  agent, I may be required to provide additional documentation as
  indicated by Imprint Analytics LLC or as set forth on our Privacy
  Policy., , â–¡ I understand that my request will be processed in
  accordance with applicable law and that certain exceptions and
  exclusions may apply to the handling of my request., , , â–¡ I
  understand that if I request BIGDBM to delete my information, such
  deletion is irreversible, and the information will be unrecoverable., ,
  , Signature: , , Print Name:, , Date:, , Instructions: complete, sign,
  and scan this form and email it to privacy@imprintanalytics.io or mail
  it to: , Imprint Analytics, Attn: Privacy, 9499 Collins Ave, #509,
  Surfside FL 33154,
  â€”----------------------------------------------------------------------------------------------------------------------------------,
  Submitting Requests:, When you submit your Right to Opt Out of Sale
  request, we will ask you to provide your name and contact information
  so that we can communicate with you regarding your request and process
  your request. , When you submit your Right to Know request or Right to
  Delete request, we will ask you to provide your name and contact
  information so that we can communicate with you regarding your request
  and process your request. , In addition, for your privacy and security
  and to prevent fraud or other harmful activities, when we receive a
  Right to Know request or a Right to Delete request, we may ask for
  information that we will use to verify your identity. For requests of
  specific pieces of personal information about a consumer, we will
  verify your identity to a reasonably high degree of certainty; whereas
  for requests to know categories of information or for requests to
  delete we will verify your identity to a reasonable degree of
  certainty. Providing accurate information that matches our records is
  necessary so that we can locate the correct information within our
  systems and among our service providers. The information we may ask you
  to provide includes your name, mailing address and either your mobile
  phone number or your email address. , Do not send us, directly or
  indirectly, any sensitive or special categories of Personal Information
  (e.g., social security numbers or other national or state identifiers,
  health information, biometric data or genetic characteristics, criminal
  background information, financial account numbers, payment card
  information, and so on) on or through the Website or otherwise. , We
  will evaluate and respond to your request to the extent required by law
  (or in our discretion if not required by law) and as permitted by our
  contracts, confidentiality obligations, and applicable laws and
  regulations. We may not be able to provide all of the information
  requested due to certain exceptions enumerated in tother applicable
  laws. If we do not have sufficient information about you to verify your
  identity, we may not be able to identify you and will be unable to
  process your request. We will attempt to verify your identity by using
  the information you submit with your request matching it with the
  information we possess about you. We may need to request additional
  information to sufficiently identify you., If you are an authorized
  agent submitting a request on behalf of a consumer, please also email
  the below information to privacy@imprintanalytics.io or attach the
  appropriate documentation to this webform., Authorized Agents, If you
  are an authorized agent operating as a business, then together with the
  consumer request, please provide the following:, Evidence that your
  business is registered to conduct business in the State of California
  or other applicable State;, A written authorization document signed and
  dated by each consumer authorizing the business as the authorized agent
  to act on behalf of each consumer in making the request;, Valid email
  address or other contact information for each consumer for our direct
  correspondence with each consumer, including as deemed necessary or
  legally required completion of an identity verification process., If
  you are an individual and acting as an authorized agent on behalf of a
  consumer, then together with the consumer request please provide:, A
  â€œpower of attorneyâ€ pursuant to California Probate Code Sections
  4121 â€“ 4130; or other USA State,, If no power of attorney is
  available, then provide:, A written authorization document signed by
  the consumer authorizing the agent to act as the authorized agent on
  behalf of the consumer; and, Valid email address or other contact
  information for each consumer for our direct correspondence with each
  consumer, including as deemed necessary or legally required completion
  of an identity verification process., â€œShine the Lightâ€ Law , In
  accordance with the California Shine the Light law, California
  residents may request certain information regarding our disclosure (if
  any) of Personal Information to third parties for their direct
  marketing purposes. Other than to third party recipients as set forth
  in this Privacy Policy (Section 4, How We Share Your Personal
  Information), or unless you request us to or consent to it, we do not
  share your Personal Information with third parties for their own direct
  marketing purposes. For any questions on these practices, please
  contact us at privacy@imprintanalytics.io., Location of Data
  Processing, All data processing activities undertaken by us take place
  in the United States., Other Important Information, Data Accuracy,
  Imprint Analytics LLC maintains quality control procedures to ensure
  the Personal Information we store is as accurate and complete as
  reasonably possible. We have developed proprietary technology to
  constantly evaluate the accuracy of the Personal Information we store,
  identify inaccurate Personal Information, and update the Personal
  Information as applicable and as reasonably practicable., Links to
  Third Party Sites, The Website may contain links to unaffiliated
  third-party sites. Imprint Analytics LLC and its affiliate sites do not
  endorse or make any representations about any third-party sites
  including any information found on such sites. We encourage you to
  review the privacy policies and terms of use of these unaffiliated
  third-party sites., Security , Imprint Analytics LLC maintains
  organizational, technical and physical security procedures, including
  those required by applicable laws, designed to protect Personal
  Information we store from accidental or unlawful destruction or
  accidental loss, damage, alteration, unauthorized disclosure or access,
  as well as all other forms of unlawful processing. Measures are taken
  to prevent unauthorized access, alteration, or dissemination of
  personal information. We also maintain physical security for our
  facilities and limit access to certain critical areas of our business.
  However, security risk is inherent in all internet and information
  technologies, and we cannot guarantee the security of your Personal
  Information., If we learn of and confirm the occurrence of a security
  incident leading to the misappropriation or accidental or unlawful
  destruction, loss, alteration, unauthorized disclosure of, or access
  to, your Personal Information transmitted, stored or otherwise
  processed on our systems that compromises the confidentiality,
  integrity or availability of your Personal Information, we may attempt
  to notify you electronically by posting a notice on the Website or by
  sending you an email or otherwise in accordance with applicable law.,
  Changes to This Policy, Imprint Analytics LLC may revise this Privacy
  Policy from time to time. We reserve the right to amend this Privacy
  Policy at any time. Any changes to this Privacy Policy will be posted
  here or other successor locations available from this page. You can
  determine when this Privacy Policy was last revised by checking the
  â€œLast Revisedâ€ legend at the bottom of this Privacy Policy., Filing
  a Complaint, If you have any complaints regarding our compliance with
  this Privacy Policy, please contact us. We will investigate and attempt
  to resolve complaints and disputes regarding use and disclosure of
  personal information in accordance with this Privacy Policy and in
  accordance with applicable law. You also have the right to file a
  complaint with a competent data protection authority., Information on
  the consumer requests that we have received, Below is additional
  information on the requests to exercise privacy rights that we have
  received from California consumers:, We have received 0 requests to
  know. We complied in whole or in part with N/A and denied N/A of these
  requests., We have received 0 requests to delete. We complied in whole
  or in part with N/A and denied N/A of these requests., We have received
  0 requests to opt out. We complied in whole or in part with N/A and
  denied N/A of these requests., The median number of days within which
  we have substantively responded to these requests is N/A., Data
  Protection Officer, Charles Harriman is our Data Protection Officer and
  may be reached via email at: [named individual]@imprintanalytics.io,
  Third-party websites, This Website may contain hyperlinks to websites
  operated by parties other than us. We provide such hyperlinks for your
  reference only. We do not control such websites and are not responsible
  for their contents or the privacy or other practices of such websites.
  It is up to you to read and fully understand their Privacy Policies.
  Our inclusion of hyperlinks to such websites does not imply any
  endorsement of the material on such websites or any association with
  their operators., Do Not Track, Do Not Track is a preference you can
  set on your browser to inform websites that you do not want to be
  tracked. We do not support Do Not Track ("DNT"). You can either enable
  or disable Do Not Track by visiting the Preferences or Settings page of
  your browser., Transferring data, We plan to transfer data to the
  United States., Questions, If you have any questions about this Privacy
  Policy, please contact us at privacy@imprintanalytics.io., , , (Cal.
  Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic
  violence, stalking and similar, a stronger and faster route than the
  ordinary consumer request)
- **What they say they collect:** All data collection practices are in
  accordance with all state and federal privacy laws

*Source: `data/registries/complete-reg-data-brokers.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
