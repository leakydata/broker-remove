# Corporate families, from the state registration filings

**One company, several brands, one index — declared in a legal document.**

Before writing to any broker on this list, check whether it belongs to a
family. It changes three things:

1. **The letter.** Name the siblings and ask for one answer covering all of
   them. One exchange can close five sites.
2. **How you read the reply.** A confirmation naming a single hostname, from
   a company that runs four, is not a confirmation — see
   `_SILENT_FAILURES.md` §40 and §70.
3. **What a negative means.** "We hold no record" from one brand says
   nothing about the shared index behind it.

## Where this comes from, and why it is stronger than the usual evidence

Data brokers operating in California must register annually and publish a
primary contact email address. A corporate family files under **one**
address. Grouping registrants by the domain of that address therefore
recovers the family structure directly, from a sworn filing rather than an
inference.

Compare the alternatives this project used before finding it:

| Evidence | Strength | Problem |
|---|---|---|
| Shared Cloudflare nameserver pair | Suggestive | Shared hosting is common and proves nothing on its own |
| Byte-identical opt-out template | Strong | Vendors sell templates; two firms can buy the same one |
| Sequential Zendesk ticket IDs across brands | Near-conclusive | Only observable after you have filed with all of them |
| **Shared statutory contact address** | **Conclusive** | Only covers brokers with a California nexus |

The last one is also the only one available **before** you write, which is
the whole point.

### The biggest one: ten sites, one LLC nobody has heard of

> **Mississippi Tornado Alley, LLC** filed a single 2026 registration naming
> CyberBackgroundChecks.com, AdvancedBackgroundChecks.com, FastBackgroundCheck.com,
> PeopleSearchNow.com, Phonebooks.com, SearchPeopleFree.com,
> SmartBackgroundChecks.com, USA-People-Search.com, USPhoneBook.com and
> FastPeopleSearch.com.

Ten consumer-facing people-search brands. Different designs, no shared corporate
footer, nothing linking them from outside. The legal entity's name appears on
none of the sites. This project had already written to five of them *separately,
as unrelated brokers*, and would have carried on doing so — collecting five
confirmations each naming one hostname while remaining listed on five other
sites.

Their contact address is a Zendesk subdomain, `mtalley.zendesk.com`. The company
has no website of its own. It exists only as the brands.

See `mississippi_tornado_alley.md` for the consolidated letter.

### The find that made the case

> **BeenVerified, Inc. registered using `privacy@moneybot5000.com`.**

Nothing on either website connects them. This project had been
corresponding with MoneyBot5000 for days as an unrelated broker.

### Two more tells in the same filings

**The name field is often a brand list.** Registrants put their whole
portfolio in it — *"Private Reports, Mugshot Look, Public Searcher"* is one
registrant naming three properties. **The website field does it too**:
`weinform.org--www.truthrecord.org` is two sites in one cell. Splitting both
yielded 632 brand names, held as leads in
`data/broker_leads.json` until each has a domain and a route.

### Caveats, stated plainly

- **A shared contact address proves a shared filer, not a shared database.**
  A parent may file for subsidiaries that run genuinely separate systems. Ask
  rather than assert: *"if these share an index, please confirm the removal
  covers all of them; if they are separate, say so and I will file
  separately."* Both answers are useful and only silence is not.
- **Absence proves nothing.** A broker with no California nexus never files.
  Vermont, Texas and Oregon run their own registries and are not yet mined.
- **Deregistration is a signal, not a deletion.** A registrant present in
  2024 and absent in 2026 may have been acquired, wound up, or simply not
  filed — and the obligation did not lapse with the paperwork.

---

## The 99 families (226 filings)

`tracked` = already in this project's registry. `NEW` = surfaced by the
filing and not present in any broker list used here.

### `equifax.com` — 7 filings, 7 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Ansonia Credit Data, Inc. | ansoniacreditdata.com | 2024 | tracked · `ansonia_credit_data` · pending |
| DataX, Ltd. | consumers.dataxltd.com | 2020-2023 | tracked · `datax` · pending |
| Austin Consolidated Holdings, Inc. | equifax.com | 2024, 2025, 2026 | tracked · `austin_consolidated` · pending |
| Austin Consolidated Holdings, Inc. | myprivacy.equifax.com | 2020-2023 | tracked · `equifax` · submitted |
| PayNet | paynet.com | 2020-2023, 2025 | tracked · `paynet` · pending |
| PayNet | sbinsights.paynetonline.com | 2024, 2026 | tracked · `paynet` · pending |
| Equifax Workforce Solutions LLC | theworknumber.com | 2020-2023, 2024, 2025, 2026 | tracked · `equifax_workforce_solutions` · pending |

### `altrata.com` — 6 filings, 6 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Altrata, Inc. | altrata.com | 2025, 2026 | tracked · `altrata` · pending |
| BoardEx, LLC | boardex.com | 2020-2023, 2024 | tracked · `boardex` · pending |
| Boardroom Insiders, Inc. | boardroominsiders.com | 2020-2023, 2024 | tracked · `boardroom_insiders` · pending |
| Relationship Science | relsci.com | 2020-2023, 2024 | tracked · `relationship_science` · pending |
| WealthEngine, Inc. | wealthengine.com | 2020-2023, 2024 | tracked · `wealthengine` · pending |
| Wealth-X, LLC | wealthx.com | 2020-2023, 2024 | tracked · `wealth_x` · pending |

### `ignitevisibility.com` — 5 filings, 5 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| EverConnect | 33mileradius.com | 2020-2023, 2024, 2025, 2026 | tracked · `33_mile_radius` · submitted |
| EverConnect | bestpickreports.com | 2024, 2025, 2026 | tracked · `everconnect` · pending |
| Five Star Rated | fivestarrated.com | 2024, 2025, 2026 | tracked · `five_star_rated` · pending |
| EverConnect | keywordconnects.com | 2020-2023, 2024, 2025, 2026 | tracked · `keyword_connects` · submitted |
| EverConnect | remodeling.com | 2020-2023, 2024, 2025, 2026 | tracked · `remodeling_com` · submitted |

### `privatereports.com` — 4 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Infomatics LLC | privatereports.com | 2024 | tracked · `privatereports` · submitted |
| Infomatics LLC | privatereports.com-mugshotlook.com | 2020-2023 | tracked · `infomatics` · pending |
| Infomatics LLC | — | 2026 | tracked · `infomatics` · pending |
| Private Reports, Mugshot Look, Public Searcher | — | 2025 | tracked · `private_reports_mugshot_look_public_searcher` · pending |

### `alescodata.com` — 3 filings, 3 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Alesco Data LLC; Response Solutions LLC; Statlistics Resou | alescodata.com | 2020-2023, 2024, 2025, 2026 | tracked · `alesco_data` · submitted |
| Response Solutions Group LLC | responsesoulutionsllc.com | 2020-2023 | tracked · `response_solutions` · pending |
| Stat Resource Group LLC DBA Statlistics | statlistics.com | 2020-2023 | tracked · `stat_resource_group_llc_dba_statlistics` · pending |

### `checksecrets.com` — 3 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Truth Now LLC | checksecrets.com | 2020-2023, 2024 | tracked · `truth_now` · pending |
| Truth Now LLC | — | 2026 | tracked · `truth_now` · pending |
| Checksecrets, PeopleSearchUSA, inmate searcher, SealedReco | — | 2025 | tracked · `checksecrets_peoplesearchusa_inmate_searcher_sealedrecords` · pending |

### `deepsync.com` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Deep Sync | deepsync.com | 2020-2023, 2024, 2025, 2026 | tracked · `deep_sync` · submitted |
| HomeData | homedata.com | 2020-2023 | tracked · `homedata` · pending |
| Accudata Integrated Marketing, LLC | — | 2026 | **NEW** |

### `eab.com` — 3 filings, 3 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Cappex.com, LLC | appily.com | 2024 | tracked · `cappex_com` · pending |
| Cappex.com, LLC | cappex.com | 2020-2023 | tracked · `cappex_com` · pending |
| EAB Global, Inc. | eab.com | 2020-2023, 2024, 2025, 2026 | tracked · `eab` · manual_required |

### `gmail.com` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| MY RENTER CHECKER LLC | myrenterchecker.com | 2020-2023 | **NEW** |
| Wisdom Media Group LLC | wisdommediagroupllc.com | 2020-2023, 2024 | tracked · `wisdom_media_group` · submitted |
| Records Finder Inc | — | 2026 | **NEW** |

### `huntclub.com` — 3 filings, 3 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Atlas | app.exploreatlas.io | 2026 | tracked · `atlas` · pending |
| Atlas | exploreatlas.io | 2025 | tracked · `atlas` · pending |
| Hunt Club Inc. | huntclub.com | 2024 | tracked · `hunt_club` · pending |

### `iqvia.com` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| IQVIA, Inc. | iqvia.com | 2020-2023, 2024 | tracked · `iqvia_digital` · pending |
| IQVIA Digital Inc. | iqviadigital.com | 2025 | tracked · `iqvia_digital` · pending |
| IQVIA Digital Inc. | — | 2026 | tracked · `iqvia_digital` · pending |

### `join5x5.com` — 3 filings, 3 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| 5x5 | 5x5coop.com | 2024, 2025 | tracked · `five_by_five` · submitted |
| 5x5 US, LLC | 5x5data.com | 2026 | tracked · `5x5` · submitted |
| 5X5 US, LLC | join5x5.com | 2020-2023 | tracked · `5x5` · submitted |

### `liftbasedata.com` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| LiftEngine | liftbasedata.com | 2025 | tracked · `liftengine` · pending |
| LiftEngine | liftengine.com | 2020-2023, 2024 | tracked · `liftengine` · pending |
| LiftEngine | — | 2026 | tracked · `liftengine` · pending |

### `moodys.com` — 3 filings, 3 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Moody's Corporation | moodys.com | 2025, 2026 | tracked · `moody_s` · pending |
| Moody's Analytics, Inc. | moodysanalytics.com | 2024 | tracked · `moody_s_analytics` · pending |
| Acquire Media U.S., LLC | newsedge.com | 2020-2023 | tracked · `acquire_media_u_s` · submitted |

### `nextwavemarketingstrategies.com` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Aged Lead Store | agedleadstore.com | 2024, 2025 | tracked · `aged_lead_store` · confirmed |
| Next Wave Marketing Strategies, Inc | nextwavemarketingstrategies.com | 2020-2023 | tracked · `aged_lead_store` · confirmed |
| agedleadstore.com | — | 2026 | **NEW** |

### `peoplesearcher.com` — 3 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| The People Searchers LLC | peoplesearcher.com | 2020-2023, 2024 | tracked · `the_people_searchers` · pending |
| The People Searchers LLC | — | 2026 | tracked · `the_people_searchers` · pending |
| SecretInfo | — | 2025 | tracked · `secretinfo` · submitted |

### `spokeo.com` — 3 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| freepeopledirectory.com, peoplewin.com, thatsthem.com | spokeo.com | 2020-2023, 2024 | tracked · `spokeo_com_freepeopledirectory_com_thatsthem_com_peoplewin_c` · pending |
| Spokeo.com; Freepeopledirectory.com; Thatsthem.com; People | — | 2026 | tracked · `spokeo_com_freepeopledirectory_com_thatsthem_com_peoplewin_c` · pending |
| Spokeo, Inc. | — | 2025 | **NEW** |

### `weinform.org` — 3 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| TruthRecord | weinform.org | 2024, 2025 | tracked · `weinform` · confirmed |
| We Inform LLC | weinform.org--www.truthrecord.org | 2020-2023 | **NEW** |
| We Inform LLC | — | 2026 | **NEW** |

### `360mediadirect.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Subdirect LLC DBA 360 Media Direct | 360mediadirect.com | 2020-2023, 2024, 2025 | tracked · `360_media_direct` · submitted |
| 360 Media Direct; bPerx; AdSmith; Subco; ClicknRead; WRSS | www360mediadirect.com | 2026 | tracked · `360_media_direct_bperx_adsmith_subco_clicknread_wrss` · submitted |

### `alliantdata.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Alliant Cooperative Data Solutions, LLC | alliantdata.com | 2020-2023 | tracked · `alliant` · confirmed |
| Alliant Cooperative Data Solutions LLC | alliantinsight.com | 2024, 2025, 2026 | tracked · `alliant_cooperative_data_solutions` · pending |

### `apollointeractive.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Apollo Interactive, LLC | apollointeractive.com | 2020-2023, 2024, 2025 | tracked · `mortgage_rates_pro_online_mortgage_loans_best_auto_insurance` · pending |
| Mortgage Rates Pro; Online Mortgage Loans; Best Auto Insur | — | 2026 | tracked · `mortgage_rates_pro_online_mortgage_loans_best_auto_insurance` · pending |

### `appscience.inc` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| App Science, Inc | appscience.ai | 2025, 2026 | tracked · `app_science` · pending |
| AppScience, Inc. | appscience.inc | 2024 | tracked · `app_science` · pending |

### `arccorp.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Airlines Reporting Corporation | arccorp.com | 2026 | tracked · `airlines_reporting` · pending |
| Airlines Reporting Corporation | www2.arccorp.com | 2025 | tracked · `airlines_reporting` · pending |

### `awl.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| All Web Leads, Insurance Quotes | awl.com | 2024, 2025 | tracked · `awl` · submitted |
| AWL Holdings, LLC | — | 2026 | **NEW** |

### `bigdbm.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| BIGDBM | bigdbm.com | 2020-2023, 2024, 2025 | tracked · `publicnsa_llc_dba_bigdbm` · pending |
| PublicNSA LLC dba BIGDBM | — | 2026 | tracked · `publicnsa_llc_dba_bigdbm` · pending |

### `biointelli.net` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Biointelli | biointelli.com | 2025, 2026 | **NEW** |
| Biointelli Corporation | — | 2024 | tracked · `biointelli` · pending |

### `buildertrend.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Buildertrend Solutions, Inc. | buildertrend.com | 2020-2023, 2024, 2025 | tracked · `buildertrend_solutions` · pending |
| Buildertrend Solutions, Inc. | — | 2026 | tracked · `buildertrend_solutions` · pending |

### `buyerlink.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Buyerlink Inc. | buyerlink.co | 2026 | tracked · `buyerlink` · pending |
| Buyerlink Inc. | buyerlink.com | 2020-2023, 2024, 2025 | tracked · `buyerlink` · pending |

### `careerbuilder.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| CareerBuilder, LLC | careerbuilder.com | 2024, 2025 | tracked · `careerbuilder` · submitted |
| CareerBuilder, LLC | hiring.careerbuilder.com | 2020-2023 | **NEW** |

### `cengage.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Cengage Learning, Inc. | cengage.com | 2025 | tracked · `gale` · submitted |
| Gale | gale.com | 2020-2023, 2024 | tracked · `gale` · submitted |

### `cision.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Brandwatch | brandwatch.com | 2020-2023, 2024, 2025, 2026 | tracked · `brandwatch` · submitted |
| Cision | cision.com | 2020-2023, 2024, 2025, 2026 | tracked · `cision` · submitted |

### `date-detective.app` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Date Detective Inc | date-detective.app | 2025 | tracked · `date_detective` · pending |
| Date Detective | — | 2026 | **NEW** |

### `definitivehc.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Definitive Healthcare | definitivehc.com | 2020-2023, 2024, 2025, 2026 | tracked · `definitive_healthcare` · pending |
| Definitive Healthcare | — | 2026 | tracked · `definitive_healthcare` · pending |

### `deloitte.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Deloitte Financial Advisory Services LLP | deloitte.com | 2020-2023, 2024, 2025, 2026 | tracked · `deloitte_financial_advisory_services` · pending |
| Deloitte Consulting LLP | — | 2026 | tracked · `deloitte_consulting` · pending |

### `dnb.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Dun and Bradstreet Inc. | dnb.com | 2020-2023, 2024, 2025, 2026 | tracked · `dun_and_bradstreet` · pending |
| Dun and Bradstreet AB | netwisedata.com | 2020-2023, 2024, 2025, 2026 | tracked · `netwise` · submitted |

### `donorbase.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| DonorBase | dataaxlenonprofit.com | 2024, 2025 | tracked · `donorbase` · pending |
| DonorBase | donorbase.com | 2020-2023, 2026 | tracked · `donorbase` · pending |

### `enformion.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Tracers; Enformion; Endato | enformion.com | 2020-2023, 2024, 2025 | tracked · `tracers_com_enformiongo` · pending |
| Tracers.com; EnformionGO | — | 2026 | tracked · `tracers_com_enformiongo` · pending |

### `erepublic.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| e.Republic, LLC | erepublic.com | 2020-2023, 2024, 2025 | tracked · `e_republic` · submitted |
| e.Republic, LLC | — | 2026 | **NEW** |

### `evs7.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Electronic Voice Services, Inc. | evs7.com | 2024, 2025 | tracked · `electronic_voice_services` · pending |
| Electronic Voice Services, Inc. | telephonelists.biz | 2020-2023, 2026 | tracked · `electronic_voice_services` · pending |

### `experian.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Audigent | audigent.com | 2024, 2025, 2026 | tracked · `audigent` · pending |
| Experian Information Solutions, Inc | experian.com | 2020-2023, 2024, 2025, 2026 | tracked · `experian_marketing` · submitted |

### `famousbirthdays.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Famous Birthdays LLC | famousbirthdays.com | 2020-2023, 2024, 2025 | tracked · `famous_birthdays` · pending |
| Famous Birthdays LLC | — | 2026 | tracked · `famous_birthdays` · pending |

### `faraday.io` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Faraday, Inc. | faraday.ai | 2024, 2025, 2026 | tracked · `faraday` · pending |
| Faraday, Inc. | faraday.io | 2020-2023 | tracked · `faraday` · pending |

### `firstdirectmarketing.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| First Direct, National List Services | firstdirectmarketing.com | 2020-2023, 2024, 2025 | tracked · `first_direct_national_list_services_firstdirect360` · pending |
| First Direct; National List Services; FirstDirect360 | — | 2026 | tracked · `first_direct_national_list_services_firstdirect360` · pending |

### `gbgplc.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Acuant, Inc. | acuant.com | 2020-2023 | tracked · `acuant` · submitted |
| IDology, Inc. | idology.com | 2020-2023 | tracked · `idology` · pending |

### `giantpartners.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| List Giant | giantpartners.com | 2020-2023, 2024, 2025 | tracked · `giant_partners` · submitted |
| Giant Partners, Inc. | — | 2026 | **NEW** |

### `healthcare.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| HealthCare, Inc. | healthcare.com | 2020-2023, 2024, 2025 | tracked · `healthcare_com` · pending |
| Healthcare.com | — | 2026 | tracked · `healthcare_com` · pending |

### `helmerprinting.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Wholesale Mail | domymail.com | 2020-2023 | tracked · `wholesale_mail` · pending |
| Wholesale Mail HP | helmerprinting.com | 2024 | tracked · `wholesale_mail_hp` · pending |

### `hivestack.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Hivestack Inc. | hivestack.com | 2020-2023, 2024, 2025 | tracked · `hivestack` · pending |
| Perion | perion.com | 2026 | tracked · `perion` · pending |

### `hubspot.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Clearbit | hubspot.com | 2024, 2025 | tracked · `hubspot` · pending |
| HubSpot, Inc. | — | 2026 | tracked · `hubspot` · pending |

### `idg.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Foundry | foundryco.com | 2025 | tracked · `foundry` · pending |
| Foundry | idg.com | 2024 | tracked · `foundry` · pending |

### `infopay.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| InfoPay, Inc | infopay.com | 2020-2023, 2024, 2025 | tracked · `infotracer_goodcar_propertychecker_entitycheck_sentinex_cour` · pending |
| InfoTracer; GoodCar; Propertychecker; EntityCheck; Sentine | — | 2026 | tracked · `infotracer_goodcar_propertychecker_entitycheck_sentinex_cour` · pending |

### `iwave.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| iWave | iwave.com | 2020-2023, 2024 | tracked · `iwave` · submitted |
| Kindsight | kindsight.io | 2025, 2026 | tracked · `kindsight` · pending |

### `kalibrate.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Kalibrate | esiteanalytics.com | 2020-2023, 2024, 2025 | tracked · `esite_analytics` · pending |
| Kalibrate | intalytics.com | 2020-2023, 2024, 2025, 2026 | tracked · `kalibrate` · pending |

### `kidslivesafe.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Kids Live Safe, Quick Public Records | kidslivesafe.com | 2025 | tracked · `kidslivesafe_com_quickpublicrecords_com` · pending |
| kidslivesafe.com, quickpublicrecords.com | — | 2026 | tracked · `kidslivesafe_com_quickpublicrecords_com` · pending |

### `l2political.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| L2, Inc | l2-data.com | 2024, 2025, 2026 | tracked · `l2_data` · submitted |
| L2, Inc. | l2political.com | 2020-2023 | tracked · `l2` · pending |

### `lead411.io` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Lead411 Corporation | lead411.com | 2020-2023, 2024, 2025 | **NEW** |
| Lead411 Corporation | — | 2026 | **NEW** |

### `leidos.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Leidos Digital Solutions, Inc. | intranetquorum.com | 2020-2023, 2024 | tracked · `leidos_digital_solutions` · pending |
| Leidos Digital Solutions, Inc. | leidosiq.com | 2025, 2026 | tracked · `leidos_digital_solutions` · pending |

### `lexisnexisrisk.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| ID Analytics LLC | idanalytics.com | 2020-2023 | tracked · `id_analytics` · pending |
| LexisNexis Risk Solutions FL Inc. | risk.lexisnexis.com | 2020-2023, 2024, 2025, 2026 | tracked · `lexisnexis_risk_solutions_fl` · pending |

### `lgads.tv` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| LG Ads Solutions | alphonso.tv | 2020-2023, 2024, 2026 | tracked · `lg_ads_solutions` · pending |
| LG Ad Solutions | lgads.tv | 2025 | tracked · `alphonso` · submitted |

### `lightcast.io` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Lightcast | lightcast.io | 2020-2023, 2024, 2025 | tracked · `lightcast` · pending |
| Economic Modeling; Rhetorik | — | 2026 | tracked · `economic_modeling_rhetorik` · pending |

### `listmatch.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Email Marketing Services, INC | listmatch.co | 2024 | tracked · `email_marketing_services` · pending |
| Email Marketing Services, Inc | listmatch.com | 2020-2023 | tracked · `email_marketing_services` · pending |

### `ltvco.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| BeenVerified.com | beenverified.com | 2024 | tracked · `beenverified` · submitted |
| BeenVerified, LLC and its subsidiaries and affiliates | — | 2026 | tracked · `beenverified_llc_and_its_subsidiaries_and_affiliates` · pending |

### `minerva.io` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Minerva | minerva.io | 2026 | tracked · `minerva` · submitted |
| Minerva BI Inc | minervabio.com | 2025 | tracked · `minerva_bi` · pending |

### `monevo.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Monevo, Inc. | monevo.com | 2024, 2025 | tracked · `monevo` · pending |
| Monevo Inc | monevo.us | 2020-2023 | tracked · `monevo` · pending |

### `monitorbase.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| MonitorBase | monitorbase.com | 2024, 2025, 2026 | tracked · `monitorbase` · pending |
| Lender Feed LC | ww3.monitorbase.com | 2020-2023 | tracked · `lender_feed_lc` · pending |

### `mtalley.zendesk.com` — 2 filings

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Mississippi Tornado Alley LLC | — | 2025 | tracked · `mississippi_tornado_alley` · pending |
| CyberBackgroundChecks.com; AdvancedBackgroundChecks.com; F | — | 2026 | tracked · `cyberbackgroundchecks_com_advancedbackgroundchecks_com_fastb` · pending |

### `myflashcloud.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| FlashIntel | flashintel.ai | 2024, 2025 | tracked · `flashintel` · submitted |
| stefan certic | myflashcloud.com | 2020-2023 | tracked · `flashintel` · submitted |

### `narvar.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Narvar, Inc | corp.narvar.com | 2026 | tracked · `narvar` · pending |
| Narvar, Inc. | narvar.com | 2025 | tracked · `narvar` · pending |

### `oan.pl` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Online Advertising Network sp. z o.o. | oan.pl | 2020-2023, 2024, 2025 | tracked · `online_advertising_network_sp_z_o_o` · pending |
| OAN; Online Advertising Network | — | 2026 | tracked · `oan_online_advertising_network` · pending |

### `omginc.xyz` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| ONLINE MEDIA GROUP INC. | omginc.xyz | 2025 | tracked · `online_media` · pending |
| MixRank | — | 2026 | tracked · `mixrank` · pending |

### `peopleconnect.us` — 2 filings

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Instant Checkmate | — | 2026 | tracked · `instantcheckmate` · submitted |
| TruthFinder | — | 2026 | tracked · `truthfinder` · submitted |

### `peoplefinders.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Peoplefinders LLC | peoplefinders.com | 2020-2023, 2024, 2025 | tracked · `findaneighborhood` · pending |
| FindANeighborhood | — | 2026 | tracked · `findaneighborhood` · pending |

### `precisely.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| PlaceIQ; PIQ | precisely.com | 2024, 2025, 2026 | tracked · `precisely` · submitted |
| Precisely | — | 2026 | tracked · `precisely` · submitted |

### `privaterecords.net` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Private Records LLC | privaterecords.net | 2020-2023, 2024, 2025 | tracked · `privaterecords` · confirmed |
| Private Records LLC | — | 2026 | **NEW** |

### `propertyreach.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Property Reach LP | propertyreach.com | 2024, 2025 | tracked · `propertyreach` · manual_required |
| LeadSherpa | — | 2026 | tracked · `leadsherpa` · pending |

### `raycdp.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Ray CDP Inc | raycdp.com | 2020-2023 | tracked · `ray_cdp` · pending |
| Ray CDP, Inc. | rayinsights.com | 2025 | tracked · `ray_insights` · pending |

### `rbarrel.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Cross Pixel | crosspixel.net | 2020-2023, 2024, 2025, 2026 | tracked · `cross_pixel` · pending |
| RainBarrel | knowertech.com | 2025, 2026 | tracked · `rainbarrel` · pending |

### `realeflow.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Realeflow LLC | realeflow.com | 2024, 2025 | tracked · `realeflow` · pending |
| Realeflow LLC | — | 2026 | tracked · `realeflow` · pending |

### `retention.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Retention.com, RB2B | retention.com | 2024, 2025 | tracked · `retention_com_rb2b` · pending |
| RETENTION.COM; RB2B | — | 2026 | tracked · `retention_com_rb2b` · pending |

### `sabio.inc` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Sabio, Inc. | sabio.inc | 2020-2023, 2024, 2025 | tracked · `sabio` · pending |
| Sabio Inc | sabioctv.com | 2026 | tracked · `sabio` · pending |

### `slashdotmedia.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Slashdot Media | slashdotmedia.com | 2020-2023, 2024, 2025 | tracked · `slashdot_media_sourceforge_voipreview_slashdot_linux_journal` · pending |
| Slashdot Media; Sourceforge; VoipReview; Slashdot; Linux J | — | 2026 | tracked · `slashdot_media_sourceforge_voipreview_slashdot_linux_journal` · pending |

### `socialgist.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Socialgist; Boardreader | socialgist.ai | 2026 | tracked · `socialgist_boardreader` · pending |
| Socialgist | socialgist.com | 2020-2023, 2024, 2025 | tracked · `socialgist` · pending |

### `sourceitmarketing.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Sourceit Technologies, Inc | sourceit.co | 2024 | tracked · `sourceit_technologies` · pending |
| SourceIT Technologies, Inc | sourceitmarketing.com | 2020-2023 | tracked · `sourceit` · confirmed |

### `spectrumlists.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Spectrum Mailing Lists | spectrumlists.com | 2020-2023 | tracked · `spectrum_mailing_lists` · submitted |
| SPECTRUM DATA | spectrummailinglists.com | 2024 | tracked · `spectrum_data` · pending |

### `spyfly.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Spyfly, Public Record Reports | spyfly.com | 2025 | tracked · `spyfly_com_publicrecordreports_com` · pending |
| spyfly.com, publicrecordreports.com | — | 2026 | tracked · `spyfly_com_publicrecordreports_com` · pending |

### `step2successmarketing.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| STEP2SUCCESS Marketing | s2smarketing.com | 2024 | tracked · `step2success_marketing` · submitted |
| STEP2SUCCESS Marketing | step2successmarketing.com | 2020-2023 | tracked · `step2success_marketing` · submitted |

### `stirista.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Stirista, 123Push, LBDigital, Media Source Solutions (MSS) | stirista.com | 2020-2023, 2024, 2025 | tracked · `stirista_123push_lbdigital_media_source_solutions_customer_p` · pending |
| Stirista; 123Push; LBDigital; Media Source Solutions; Cust | — | 2026 | tracked · `stirista_123push_lbdigital_media_source_solutions_customer_p` · pending |

### `targetsmart.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| TargetSmart Communications LLC | privacy.targetsmart.com | 2020-2023 | tracked · `targetsmart_communications` · pending |
| N/A | targetsmart.com | 2024, 2025, 2026 | tracked · `n_a` · pending |

### `teads.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Outbrain | outbrain.com | 2020-2023, 2024, 2025, 2026 | tracked · `outbrain` · submitted |
| Teads Inc | teads.com | 2025, 2026 | **NEW** |

### `teamdms.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| DataDirect Marketing Solutions, Inc. | datadirectmarketing.com | 2020-2023, 2024 | tracked · `data_direct_marketing` · failed |
| Direct Marketing Solutions, Inc. | teamdms.com | 2024, 2025 | tracked · `direct_marketing_solutions` · pending |

### `techtarget.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Informa TechTarget | techtarget.com | 2020-2023, 2024, 2025 | tracked · `informa_techtarget` · pending |
| Informa TechTarget | — | 2026 | tracked · `informa_techtarget` · pending |

### `therooftop.io` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Rooftop Digital, LLC | rooftopdigital.com | 2024, 2025 | tracked · `rooftop_digital` · pending |
| Rooftop Digital | therooftop.io | 2020-2023 | **NEW** |

### `unearthcampaigns.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Unearth Campaigns, LLC | unearthcampaigns.com | 2020-2023, 2024, 2025 | tracked · `unearth_campaigns` · manual_required |
| Atlas Influence Targeting | — | 2026 | tracked · `atlas_influence_targeting` · pending |

### `ups.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| UPS Capital Corporation | upscapital.com | 2024, 2025 | tracked · `ups_capital` · pending |
| UPS Capital Corporation | — | 2026 | tracked · `ups_capital` · pending |

### `usinfosearch.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Martin Data LLC | martin-data.com | 2020-2023 | tracked · `martin_data` · pending |
| USinfoSearch.com | usinfosearch.com | 2024 | tracked · `usinfosearch_com` · pending |

### `verisk.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Verisk Marketing Solutions | marketing.verisk.com | 2024 | tracked · `verisk_marketing_solutions` · pending |
| Verisk Marketing Solutions | verisk.com | 2025 | tracked · `verisk_marketing_solutions` · pending |

### `versium.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Versium Analytics Inc. | versium.com | 2020-2023, 2024, 2025 | tracked · `versium_analytics` · pending |
| Versium Analytics, Inc. | — | 2026 | tracked · `versium_analytics` · pending |

### `zetaglobal.com` — 2 filings, 2 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| LiveIntent | liveintent.com | 2020-2023, 2024, 2025, 2026 | tracked · `liveintent` · submitted |
| Zeta Global | zetaglobal.com | 2020-2023, 2024, 2025, 2026 | tracked · `zeta_global` · pending |

### `ziffdavis.com` — 2 filings, 1 distinct sites

| Registrant | Site | Years filed | Status here |
|---|---|---|---|
| Ziff Davis LLC | ziffdavis.com | 2025, 2026 | tracked · `ziff_davis` · pending |
| Campaigner; SMTP | — | 2026 | tracked · `campaigner_smtp` · pending |

---

*Generated by `scripts/build_families_doc.py` from
`data/broker_families.json`. Refresh with*
*`scripts/import_state_registries.py --fetch --families`.*

---

## Appendix: the acquisition named in the mailbox itself

Azerion's registered contact is **`dpo_hybridtheory@azerion.com`** — the local
part names Hybrid Theory, a business Azerion acquired, while the domain is the
parent's.

**A local-part naming a different company is a disclosed acquisition.** It is
weaker evidence than a shared statutory contact (it could be a legacy alias
nobody renamed) but it is free, it is visible before you write, and it tells you
two things worth acting on:

1. **Which entity actually holds the data.** A request addressed to the parent in
   general terms may be answered for the parent's own systems while the acquired
   business's dataset sits untouched. Name both.
2. **That there is probably a suppression boundary**, since acquired platforms
   are frequently still running on their own infrastructure. Ask directly:
   *does a suppression recorded here reach the other, or stop at your systems?*
   Both answers are useful and only the assumption is dangerous.

**Also read the prefix.** `dpo_` signals a European data protection function, so
a US request sent there risks being answered under the GDPR — or filed as
out-of-scope. State the governing law in the first paragraph:

> I am a United States resident and this request is made under US state law, not
> the GDPR. Your registered contact is a `dpo_` address, which usually signals a
> European function, so please route this to whoever handles US state privacy
> requests if that is someone else.

Compare Experian's `ca_drop_audigent@experian.com` in the appendix below — same
shape, parent domain plus acquired-brand local part, and there the mailbox turned
out to be unmonitored. **A brand-named local part is a lead about corporate
structure and says nothing about whether anyone reads it.**

---

## Appendix: the legal name nobody would search for

Registrations are filed under **legal entity names**, and consumers know
**brands**. Where the two differ, the company is effectively invisible in the
state registry to anyone searching by the name they recognise:

| Registered as | Known as |
|---|---|
| Baron App, Inc. | **Cameo** |
| Predictive Pop, Inc. | **Audigent** |
| Mississippi Tornado Alley, LLC | ten people-search brands |
| B.I Science (2009) Ltd | biScience |

This cuts both ways for the work here.

**Against you:** searching the registry for a brand you want to check will miss
it. There is no reliable brand-to-entity index, so the only safe approach is to
import the whole registry and match on domain rather than on name — which is what
`import_state_registries.py` does, and why it caught Cameo at all.

**For you:** the mismatch is itself a finding. A consumer-facing product filing
as a data broker under an unfamiliar legal name is asserting that it sells or
shares personal information about people **it has no direct relationship with**.
That is the statutory trigger for registration. So a brand you have never used is
still worth writing to, and the letter can say so plainly:

> I do not believe I have used your service, and if you hold nothing that is
> entirely plausible. But the registration means you have determined you meet the
> definition of a data broker — which is to say you sell or share personal
> information about people with whom you do not have a direct relationship. That
> is exactly the category I fall into.

That framing pre-empts the obvious brush-off ("you have no account with us") and
turns the registration itself into the justification for asking.

**Tell them about the mismatch.** Most companies do not realise their filing is
unfindable by brand. It costs a sentence and it is the kind of thing only an
outsider notices.

---

## Appendix: the refusal autoreply that lists the family

AutoWeb's privacy address refuses email — *"Email is not a designated method for
submitting a California privacy rights request"* — and then, helpfully, lists
where to go instead:

> **Buyerlink** · form at `buyerlink.co/do-not-sell-or-share-my-personal-information` · 1-888-821-1041
> **AutoWeb** · OneTrust webform · (800) 267-2015

**Two brands, one privacy desk, disclosed in a bounce.** Nothing on either site
announces the relationship; the autoreply does, because a shared desk naturally
answers for everything it covers.

**This is a discovery mechanism, not just an inconvenience.** A refusal that
routes you onward has to name the destinations — and a company with siblings will
name all of them, because the autoresponder does not know which brand you wrote
about. So:

- **Read every "use our form instead" reply for the list**, not just for the one
  link you need. The extra entries are free family intelligence.
- **The reply also gives you each brand's own channel**, which is more than the
  registry provides. Here it produced two forms and two toll-free numbers that no
  filing carried.

Weaker evidence than a shared statutory contact — a holding company might route
several genuinely separate businesses through one desk — so ask rather than
assert. But the routing itself is a fact you can act on immediately: submit to
both, and ask whether one suppression covers the other.

---

## Appendix: the acquirer's mailbox, one channel per acquired brand

A parent that has bought several data companies may run **one privacy function
with a dedicated address per brand**. Experian does:

| Registrant (legal name) | Trading as | Registered contact |
|---|---|---|
| Experian Information Solutions, Inc. | Experian Marketing | `ca_drop_fsd@experian.com` |
| **Predictive Pop, Inc.** | **Audigent** | `ca_drop_audigent@experian.com` |

Nothing on audigent.com announces the relationship, and "Predictive Pop, Inc."
appears nowhere on the site — the same shape as Mississippi Tornado Alley above.
The `ca_drop_` prefix marks these as DELETE Act channels.

**This is good practice on the broker's part and a trap for the tooling.** Good,
because a per-brand mailbox means a request lands with the team that holds the
data rather than in a general queue. A trap, because the duplicate-address guard
in `queue_batch.py` keys on the **full address**, not the domain — so these two
correctly stay separate and both get letters, which is right. Had the parent used
one shared address for both brands, the guard would have held the second back and
the sibling would have needed raising inside the first thread instead.

**What to do:** name the relationship in the letter rather than pretending not to
notice it, write to each brand's channel separately, and ask the one question
that matters — *does a suppression recorded here cover the sibling, or are these
genuinely separate datasets?* Both answers are useful; only the assumption is
dangerous.

---

## Appendix: a family tell the filings miss — one DSAR tenant, two brands

The registration filings recover families that share a *contact address*. They
cannot see families that file separately and then route both filings into **one
privacy-platform tenant**.

Observed 2026-08-23/24:

| | ROR Partners | ActivImpact |
|---|---|---|
| Registered contact | `privacy@rorpartners.com` | `privacy@activimpact.ai` |
| Registered separately in CA | yes | yes |
| OneTrust request ID | **L7JE3RVPKK** | **L7JE3RVPKK** |

One request was submitted. ROR Partners issued the ID and sent the verification
link from `rorpartners-privacy.my.onetrust.com`. A day later **ActivImpact**
emailed a consumer access report citing *the same request ID*.

OneTrust request IDs are generated per tenant. Two brands answering to one ID
means one tenant and one privacy operation behind both — and **the contact-address
method would never have found it**, because each brand dutifully registered its
own address.

**How to use it.** Record the request ID from every DSAR platform
acknowledgement, the same way ticket numbers are recorded for help desks. A
single ID means nothing; the second brand quoting it is the finding. This applies
to OneTrust, Ketch, DataGrail, Transcend, Osano and Securiti alike — anywhere a
vendor issues a tenant-scoped reference.

**How strong is it?** Stronger than a shared template, weaker than a shared
statutory contact. A tenant can in principle be shared by a parent servicing
subsidiaries that hold genuinely separate databases — so ask, in the usual form:
*"Both of you have quoted request L7JE3RVPKK. Does one deletion cover both
entities' records, or do I need to file separately?"* The deflating answer is
useful and should be offered as acceptable.

**One caution.** A shared tenant also means a request submitted to one brand may
be *silently scoped* to that brand only, while the platform shows both. Do not
assume coverage from the shared ID — that is the same scoped-confirmation error
as §40, arriving through a vendor rather than a hostname.
