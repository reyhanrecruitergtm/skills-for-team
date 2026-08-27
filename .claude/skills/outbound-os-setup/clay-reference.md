# Clay Setup Reference

Quick reference for building TAM tables and playbooks in Clay. Use this when configuring company searches, enrichment waterfalls, and filter logic.

---

## Company Search Filters

### Industries

Clay uses LinkedIn's official Industry Codes V2 taxonomy. **Always use exact names from the verified list below — do not guess or approximate.** Using wrong industry names silently returns no results.

**Source:** Official LinkedIn/Microsoft Learn taxonomy + Tim Queen's 241-category flat list (2026-03-14)

---

#### Quick Reference by Niche

| Client Niche | Clay Industries to Select |
|---|---|
| Tech / SaaS / AI | `Software Development`, `Technology, Information and Internet`, `IT Services and IT Consulting` |
| Fintech | `Financial Services`, `Banking`, `Investment Management`, `Insurance` |
| Healthtech / MedTech | `Hospitals and Health Care`, `Medical Practices`, `Medical Equipment Manufacturing`, `Biotechnology Research` |
| Deeptech / Research | `Research Services`, `Nanotechnology Research`, `Biotechnology Research` |
| Cybersecurity | `Computer and Network Security`, `Data Security Software Products` |
| Data / Analytics | `Data Infrastructure and Analytics`, `Business Intelligence Platforms` |
| Professional Services | `Business Consulting and Services`, `Accounting`, `Legal Services`, `Operations Consulting` |
| E-commerce / Retail | `Retail`, `Retail Apparel and Fashion`, `Retail Groceries` |
| Manufacturing | `Manufacturing`, `Industrial Machinery Manufacturing`, `Computers and Electronics Manufacturing` |
| Construction | `Construction`, `Nonresidential Building Construction`, `Residential Building Construction` |
| Real Estate | `Real Estate`, `Real Estate Agents and Brokers`, `Leasing Non-residential Real Estate` |
| Media / Marketing | `Advertising Services`, `Media Production`, `Public Relations and Communications Services` |
| Logistics | `Transportation, Logistics, Supply Chain and Storage`, `Warehousing and Storage`, `Freight and Package Transportation` |
| Staffing / Recruiting | `Staffing and Recruiting`, `Executive Search Services`, `Temporary Help Services` |
| Education | `Higher Education`, `E-Learning Providers`, `Professional Training and Coaching` |
| VC / Private Equity | `Venture Capital and Private Equity Principals`, `Investment Banking`, `Investment Management` |

---

#### Full 241-Category Flat List (Copy-Paste Safe)

These are the exact values Clay accepts. Copy-paste directly — spelling and capitalisation matter.

Abrasives and Nonmetallic Minerals Manufacturing, Accessible Architecture and Design, Accessible Hardware Manufacturing, Accounting, Administration of Justice, Advertising Services, Air Water and Waste Program Management, Alternative Dispute Resolution, Alternative Fuel Vehicle Manufacturing, Appliances Electrical and Electronics Manufacturing, Architecture and Planning, Armed Forces, Artists and Writers, Audio and Video Equipment Manufacturing, Aviation and Aerospace Component Manufacturing, Banking, Bars Taverns and Nightclubs, Bed-and-Breakfasts Hostels Homestays, Beverage Manufacturing, Biotechnology Research, Blockchain Services, Blogs, Book and Periodical Publishing, Broadcast Media Production and Distribution, Business Consulting and Services, Business Content, Business Intelligence Platforms, Chemical Manufacturing, Civic and Social Organizations, Civil Engineering, Climate Data and Analytics, Climate Technology Product Manufacturing, Community Development and Urban Planning, Computer and Network Security, Computer Games, Computer Hardware Manufacturing, Computer Networking Products, Computers and Electronics Manufacturing, Construction, Consumer Goods Rental, Consumer Services, Cosmetology and Barber Schools, Courts of Law, Dairy Product Manufacturing, Data Infrastructure and Analytics, Data Security Software Products, Defense and Space Manufacturing, Design Services, Desktop Computing Software Products, Digital Accessibility Services, E-Learning Providers, Education Administration Programs, Entertainment Providers, Environmental Quality Programs, Environmental Services, Events Services, Executive Offices, Facilities Services, Farming, Financial Services, Fisheries, Food and Beverage Manufacturing, Food and Beverage Services, Footwear and Leather Goods Repair, Freight and Package Transportation, Fruit and Vegetable Preserves Manufacturing, Fuel Cell Manufacturing, Fundraising, Furniture and Home Furnishings Manufacturing, Gambling Facilities and Casinos, Glass Ceramics and Concrete Manufacturing, Golf Courses and Country Clubs, Government Administration, Government Relations Services, Graphic Design, Ground Passenger Transportation, Health and Human Services, Higher Education, Historical Sites, Home Health Care Services, Hospitality, Hospitals, Hospitals and Health Care, Hotels and Motels, Household Services, Housing and Community Development, Housing Programs, Human Resources Services, Individual and Family Services, Industrial Machinery Manufacturing, Information Services, Insurance, Insurance and Employee Benefit Funds, Interior Design, International Affairs, International Trade and Development, Internet News, Internet Publishing, Investment Banking, Investment Management, IT Services and IT Consulting, IT System Custom Software Development, IT System Data Services, IT System Installation and Disposal, IT System Operations and Maintenance, IT System Testing and Evaluation, IT System Training and Support, Janitorial Services, Landscaping Services, Language Schools, Laundry and Drycleaning Services, Law Enforcement, Law Practice, Leasing Non-residential Real Estate, Leasing Residential Real Estate, Legal Services, Legislative Offices, Libraries, Loan Brokers, Machinery Manufacturing, Manufacturing, Maritime Transportation, Market Research, Media and Telecommunications, Media Production, Medical and Diagnostic Laboratories, Medical Equipment Manufacturing, Medical Practices, Mental Health Care, Metal Valve Ball and Roller Manufacturing, Mining, Mobile Gaming Apps, Motor Vehicle Manufacturing, Motor Vehicle Parts Manufacturing, Movies Videos and Sound, Museums Historical Sites and Zoos, Musicians, Nanotechnology Research, Natural Gas Distribution, Natural Gas Extraction, Newspaper Publishing, Non-profit Organizations, Nonmetallic Mineral Mining, Nonresidential Building Construction, Nuclear Electric Power Generation, Nursing Homes and Residential Care Facilities, Office Administration, Oil and Gas, Oil Extraction, Online Audio and Video Media, Operations Consulting, Optometrists, Outpatient Care Centers, Outsourcing and Offshoring Consulting, Packaging and Containers Manufacturing, Paper and Forest Product Manufacturing, Personal and Laundry Services, Personal Care Product Manufacturing, Pharmaceutical Manufacturing, Philanthropic Fundraising Services, Photography, Physical Occupational and Speech Therapists, Political Organizations, Primary and Secondary Education, Printing Services, Professional Organizations, Professional Training and Coaching, Public Health, Public Policy Offices, Public Relations and Communications Services, Ranching, Real Estate, Real Estate Agents and Brokers, Recreational Facilities, Religious Institutions, Renewable Energy Power Generation, Renewable Energy Semiconductor Manufacturing, Research Services, Restaurants, Retail, Retail Apparel and Fashion, Retail Art Dealers, Retail Art Supplies, Retail Books and Printed News, Retail Groceries, Retail Luxury Goods and Jewelry, Retail Motor Vehicles, Retail Office Equipment, Retail Recyclable Materials & Used Merchandise, Security and Investigations, Security Guards and Patrol Services, Shuttles and Special Needs Transportation Services, Social Networking Platforms, Software Development, Space Research and Technology, Spectator Sports, Sporting Goods Manufacturing, Staffing and Recruiting, Taxi and Limousine Services, Technical and Vocational Training, Technology, Information and Internet, Telecommunications, Textile Manufacturing, Think Tanks, Tobacco Manufacturing, Translation and Localization, Transportation Programs, Transportation Logistics Supply Chain and Storage, Travel Arrangements, Truck Transportation, Urban Transit Services, Utilities, Utilities Administration, Utility System Construction, Vehicle Repair and Maintenance, Venture Capital and Private Equity Principals, Veterinary Services, Vocational Rehabilitation Services, Warehousing and Storage, Waste Collection, Waste Treatment and Disposal, Wellness and Fitness Services, Wholesale, Wholesale Alcoholic Beverages, Wholesale Apparel and Sewing Supplies, Wholesale Building Materials, Wholesale Chemical and Allied Products, Wholesale Food and Beverage, Wholesale Footwear, Wholesale Import and Export, Wholesale Luxury Goods and Jewelry, Wholesale Motor Vehicles and Parts, Wholesale Petroleum and Petroleum Products, Wholesale Raw Farm Products, Wind Electric Power Generation, Wineries, Wireless Services, Writing and Editing, Zoos and Botanical Gardens

---

#### Industries That Do NOT Exist in Clay (Common Hallucinations)

Never use these — they will return no results:

| Wrong (Do Not Use) | Correct Equivalent |
|---|---|
| Artificial Intelligence | `Software Development` or `Technology, Information and Internet` |
| Computer Software | `Software Development` |
| Information Technology & Services | `IT Services and IT Consulting` |
| Internet | `Technology, Information and Internet` |
| Hospital & Health Care | `Hospitals and Health Care` |
| Pharmaceuticals | `Pharmaceutical Manufacturing` |
| Biotechnology | `Biotechnology Research` |
| Management Consulting | `Business Consulting and Services` |
| Marketing & Advertising | `Advertising Services` |
| Logistics & Supply Chain | `Transportation, Logistics, Supply Chain and Storage` |
| Mechanical or Industrial Engineering | `Industrial Machinery Manufacturing` or `Machinery Manufacturing` |

> Rule: If an industry name isn't in the 241-category flat list above, it does not exist. Do not use it.

---

### Headcount Ranges (Clay standard bands)

| Label | Range |
|---|---|
| Micro | 1–10 |
| Small | 11–50 |
| SME Lower | 51–200 |
| SME Upper | 201–500 |
| Mid-market | 501–1,000 |
| Enterprise lower | 1,001–5,000 |
| Enterprise upper | 5,001–10,000 |
| Large enterprise | 10,001+ |

Most recruitment clients target **51–500** (SME). Adjust based on intake.

---

### Location Filters

Clay supports:
- **Country** (e.g. Germany, United Kingdom, United States)
- **Region / State** (e.g. Bavaria, London, California)
- **City** (e.g. Munich, Berlin, Manchester)

For DACH markets: select Germany + Austria + Switzerland separately.
For UK: "United Kingdom" covers England, Scotland, Wales, Northern Ireland.

---

### Company Description Keyword Logic

Clay searches the company's LinkedIn description field.

**Inclusion keywords** (company must match):
- Use single words or short phrases: hiring, scaling, Series B, backed by
- Clay treats multiple keywords as OR logic by default
- To approximate AND logic: add separate filter rows and cross-reference in formula column

**Exclusion keywords** (filter out):
- Common exclusions: staffing, recruitment agency, NHS, public sector, charity, non-profit
- Add these in Clay's "does not contain" field

**Output format rule:** Always output keywords, titles, industries, and locations as plain comma-separated lists — no quotation marks, no bullet points per item. Example:
```
Industries:             Real Estate, Leasing Non-residential Real Estate, Leasing Residential Real Estate
Headcount:              51–200, 201–500
Location:               Germany
Description includes:   employer brand, talent acquisition, EVP, candidate experience
Description excludes:   staffing agency, recruitment agency, RPO, public sector, NHS, charity
Contact titles:         Head of Employer Brand, Director of Talent Acquisition, Recruitment Marketing Manager, VP People
```

---

## Enrichment Waterfall Logic

Use waterfall enrichment when a single data provider won't fill all rows. Clay tries providers in order and stops when data is found.

**Standard contact email waterfall (LOCKED 2026-05-24 — Prospeo PRO plan, 15k credits/mo at zero cost):**
1. **Prospeo** (own API key, PRO plan) — primary. 15k free credits/mo via content partnership, burn them first.
2. **Apollo** (own API key) — second pass for whatever Prospeo missed. Highest match rate on US/EU B2B work emails.
3. **Apify** (LinkedIn scrape) — third pass for LinkedIn URLs that neither resolved.
4. SalesQL (own API key) — fourth fallback for personal email + direct dial.
5. Findymail / Hunter.io — last-resort paid waterfall step.
6. Clay native — only if all own-key sources miss.

**Standard company data waterfall:**
1. Clay native LinkedIn enrichment
2. Clearbit (company details, tech stack, headcount)
3. Bombora (intent data — enterprise only)

> Rule: Apollo + Prospeo run first (own keys, near-zero cost). Prospeo PRO gives us 15k credits/month via the content partnership — burn them, don't hoard. Memory: `reference_prospeo_api.md`.

---

## Credit Cost Reference (New Pricing — post 2026-03-11)

| Operation | Credits |
|---|---|
| Company LinkedIn enrichment | 1 data credit |
| Person LinkedIn enrichment | 1 data credit |
| LinkedIn Jobs lookup | 1 data credit |
| Email find (Clay native) | 1 data credit |
| Email find (own Prospeo key) | 0 data credits (action only) |
| AI column (own OpenAI key) | 0 data credits (action only) |
| AI column (Clay AI) | Variable — charged per token |

**Target:** Keep playbooks at 3–4 data credits/row by using own API keys for email + AI.

---

## Alternate Sources (When Clay TAM < 3,000 Companies)

| Source | How to Use |
|---|---|
| Apollo.io | Company search with same ICP filters → export CSV → import into Clay |
| LinkedIn Sales Nav | Company search → save list → export via third-party tool (Phantombuster, Evaboot) |
| LinkedIn Manual | Search + filter → export connection list or use browser extension |
| ZoomInfo | Enterprise — only if client has access |
| Crunchbase | Good for funded/VC-backed companies — export and import to Clay |

> Flag to Reyhan if TAM estimate is < 3k. Present alternate sources before starting enrichment.

---

## Common Mistakes to Avoid

- **Too broad industry selection** → inflated TAM with wrong company types. Use keyword exclusions to clean up.
- **Missing exclusion keywords** → staffing agencies, public sector, or charities polluting the list.
- **No headcount filter** → Clay returns solo operators and enterprises that aren't relevant.
- **Running enrichment before client approves TAM** → wastes credits on unapproved companies.
- **Single data provider for email** → high miss rate. Always use waterfall.
- **Defaulting to industry filters when the ICP is function-based** → if the client targets "any company large enough to have X team", industry is irrelevant. Use headcount + people title search instead (see Giles Guest lesson below).

---

## TAM Build Learnings (Live Client Log)

This section captures lessons from real TAM builds. Read this before configuring a new client's table.

---

### Client: Giles Guest — Recruitment Marketing Agency (Mar 2026)

**What they sell:** AI Perception Audit of recruitment brands (£10k). Targets Employer Brand, Talent Acquisition, and Recruitment Marketing leaders.

**Mistake made:** Initially filtered by industries (HR Services, Advertising, Business Consulting). This was completely wrong.

**Why it was wrong:** Giles targets employers — ANY company large enough to have a dedicated EB/TA function. Lloyd's Bank (Banking), IBM (Tech), Microsoft (Software) are all valid targets. Industry is irrelevant.

**Correct approach:**
- No industry filter
- Headcount: 1,001+ employees (top ~2,000 UK companies)
- Location: United Kingdom
- Use **people-first search** — find contacts with "Employer Brand", "Talent Acquisition", or "Recruitment Marketing" in title, then reverse-enrich the company

**Rule learned:** When the client says "any company large enough to have X team/function", skip industry filters entirely. The signal lives in the contact title, not the company's sector.

**Estimated TAM:** 15,000–25,000 contacts across the top 2,000 UK employers. No alternate sources needed.

---

### Client: Oliver — German Property Management (Mar 2026)

**What they sell:** Recruitment/ops support for property management companies in Germany.

**ICP:** German property management and real estate companies, 50–500 employees.

**Clay industries used:** `Real Estate`, `Leasing Non-residential Real Estate`, `Leasing Residential Real Estate`, `Real Estate Agents and Brokers`

**Correct approach:**
- Industry filter was the right lever here — niche is sector-specific
- Location: Germany
- Headcount: 51–500 (SME Lower + SME Upper bands)
- Excluded: open jobs trigger (client didn't want this signal)

**Rule learned:** When the client is niche-specific (only works with one sector), industry filter is the primary lever. When the client is function-specific (works with any sector that has X team), people title is the primary lever.

---

### Key Decision Framework: Industry Filter vs. People Title Filter

Use this to decide which approach to take before building any TAM:

| Client type | Right approach |
|-------------|---------------|
| Targets a specific sector (e.g. property, fintech, healthcare) | Company search → industry filter + headcount + location |
| Targets any company with a specific function (e.g. EB team, TA team, dev team) | People search → title filter + company headcount + location |
| Targets a specific role type across all industries (e.g. any CTO) | People search → title + seniority + headcount |
| Targets funded/growing companies | Company search → Crunchbase/funding signal + headcount, no industry needed |

Always ask: **"Is the ICP defined by what the company does, or by who exists inside the company?"**

---

### Client: Oliva Talent — German Tech Recruiting (Mar 2026)

**Contact:** Timur Mukhamedzhanov
**What they sell:** Recruitment services for tech companies in Germany — placing Data Engineers, AI Engineers, DevOps, Cloud, ML, BI, and niche backend developers.
**Start date:** 4th March 2026

**ICP:** Small-to-mid German tech companies (10–200 employees) that are growing but lack internal HR/recruitment infrastructure. Sweet spot is 10–20 employees in IT Services or Data. Must have open vacancies in tech roles. Located in Germany, preference for Bayern.

**Exclusions:** IT outstaffing firms, offshore staffing companies, consulting agencies, recruiting firms, education platforms, event businesses, freelance collectives, communities.

**Scoring used:** 1–3 scale (see scoring prompt in this section). Score 3 = 10–20 employees, Bayern, <6 years old, open IT vacancy in target roles, no HR department, poor employer brand, recent headcount growth.

**Contact personas:**
- Larger companies (20+): HR vertical — Recruiter, Talent Acquisition, HR Manager, Talent Partner, Recruitment Partner (use German equivalents)
- Smaller companies (<20): Leadership — CEO, CTO, COO, Head of IT, Head of Engineering, Head of Software Development, Team Lead, Data Engineering Lead

**Industries used:** IT Services and IT Consulting, Data Infrastructure and Analytics, Software Development, Technology, Information and Internet, Computer and Network Security, IT System Custom Software Development

**Rule learned:** Open vacancy is the primary buying signal for this client. Run LinkedIn Jobs enrichment before scoring — a company with no open roles scores maximum 1 regardless of other signals. Layer HR headcount ratio as a secondary signal (HR staff < 4% of total headcount = high pain).
