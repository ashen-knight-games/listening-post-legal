# Privacy Policy

**Applies to:** the ListenPost demo and full game on Steam
**Studio:** Ashen Knight Games
**Version:** 1.0 — effective 2026-09-09
**Contact:** support@ashenknightgames.com

---

## In short

- The game logs your gameplay patterns—specifically your answers, completion times, and where you encounter difficulties. It strictly avoids accessing any text or data outside the game environment.
- **Gameplay logs require your consent**. They are not transmitted or saved locally unless you explicitly opt in, and selecting "No" or "Ask me later" stops the recording. The only exceptions are the three reports in section 3: a problem report you send yourself, and the anonymous crash and exit reports (both of which also stop once you choose "No").
- **For players in the EU, EEA, UK, Switzerland, or mainland China**: All data is **entirely anonymized**. We have no way to link records to specific individuals or determine if multiple logs belong to the same user.
- Opting out **does not alter your experience**. All game features remain fully accessible and unchanged.
- **A problem report you fill in yourself** sends us the information you provided (section 3).
- **If the game did not shut down properly**, a crash report is sent the next time it starts (section 3; how much it contains depends on your answer and your region, and none is sent if you chose "No").
- **When you close the game normally**, it sends one anonymous exit report saying where you stopped (the screen, the battle or the prologue step) plus a few counts (section 3; never with an account, and none is sent if you chose "No").

---

## 1. Who we are

Ashen Knight Games ("we") acts as the data controller for the information covered under this policy regarding our game, ListenPost. For any inquiries, please contact us directly at **support@ashenknightgames.com**.

Our game is distributed exclusively via Steam. Because Valve manages all purchasing operations, we never gain access to your financial data, email address, or Steam account details during the transaction.

## 2. What we collect, and only if you agree

**Following your initial battle**, a one-time prompt will ask if you consent to sharing your gameplay logs. Your options are **No, Ask me later, or Yes**.

- Choosing **Yes** transmits the recorded data to us, which includes the match you just finished; if the prologue was played during this same launch, it is also included.
- Choosing **No** permanently deletes the logged session, and the prompt will never appear again.
- Opting to **Ask me later** wipes the current log and defers the question to your next session. If you choose this option a second time, it counts as "No" and the system stops prompting you entirely.
- Until an explicit **Yes** is given, your gameplay log resides strictly within your system's RAM. It will never be written to your local drive or broadcasted over the network.

### What a record contains

- **Standard Question Data**: For every quiz question answered, the game tracks the target word, its vocabulary frequency tier, sentence category, and your final answer outcome. It also monitors behavioral metrics like audio replay counts, use of the slow-reading feature, hint triggers, first-try accuracy, and time spent per item.
- **Friction Points ("Stuck" Situations)**: When a hint is displayed, we capture deeper diagnostics. This includes the full text of the sentence, the precise playback profile of every audio clip (so we can reproduce exactly what you heard), the start and stop time of each clip, and the concurrent tactical state (current tower health and enemy count). Outside the anonymous regions defined in Section 4, the record additionally includes your keystroke events on a timeline, flagging each input as correct or incorrect.
- **Performance metrics**: How long your machine takes to generate speech, load times, and voice queue stability. Outside the anonymous regions defined in Section 4, this also includes CPU and graphics adapter model names, core count and total system memory. **We record this in order to tune speech generation for different hardware**, so that later updates can deliver smoother playback.
- **Match Context**: Each battle session logs global parameters including the active chapter, level, difficulty configurations, your calculated vocabulary proficiency, the software build version, and an event timeline charting enemy waves, target spawns, and damage sustained.

### What we never collect

- Your name, email address, Steam profile, friends, or anything from your Steam account other than what is described in section 4.
- Anything you type outside of answering questions — including the name you give a save slot.
- We collect none of the above, except what you choose to provide in a problem report yourself (section 3).
- Your IP address. **We do not store it.** Our hosting provider necessarily processes it briefly in order to deliver the request, but we never read it, never write it to a file, and request logging is switched off.
- Any file or program on your computer, and any hardware detail beyond the specific items listed above.

## 3. Problem reports, crash reports and exit reports

Problem reports, crash reports and exit reports are collected separately from the gameplay logs. None of them waits for the prompt in section 2, because each has its own reason: a problem report is something you write and choose to send yourself, a crash report only exists because the game did not get to shut down properly, and an exit report is the one thing that tells us where people stop before they ever reach that prompt.

### Problem reports

The Options screen and the pause menu in battle have a **Report a problem** button. You choose a category, write what you want to report, and press **Send**.

A report contains:

- The category and the text you wrote. A report carries nothing that identifies you, so we cannot single out one report to delete it later. Please do not write your name, email address or anything private.
- The state of the game at that moment: the current screen, level and wave, the game version, the interface language, how long the game had been running, and the time you sent it (your local time, with its offset from UTC).
- Device information, **only if you set "Include device info" to Yes**. The default is No. When it is on, the report also carries your CPU and graphics adapter model names, core count, system memory, operating system version, window and screen size, and the current frame rate and memory use. This is the same hardware description as in section 4, and it is what lets us reproduce stutter, display and performance problems.

A problem report never contains your Steam ID number, so even outside the anonymous regions it remains anonymous.

### Crash reports

While the game runs it keeps a small running-state record, refreshed every few seconds with the current screen, level and wave. When the game closes normally, that file is deleted. If it is still there when the game starts, the previous session is treated as a crash and the game sends one crash report about it. Each crash produces one report, and the game does not ask you about it.

What a crash report contains follows the regions in section 4 and the choice you made in section 2:

- **If you chose "No"** to sharing gameplay logs, no crash report is sent at all.
- **If you chose "Yes" and you are outside the anonymous regions in section 4**: the report contains the last recorded game state, level and wave, the frame rate and memory use at the last refresh, the play time, the local time of the restart that sent the report, the game version, your CPU and graphics adapter model names, core count and system memory, your Steam ID number, and the last part of the game's own log file (at most 16 KB). It goes through the same queue as your gameplay logs: if it cannot be sent, it is kept on your computer until it goes through.
- **In every other case** (you have not been asked yet, you chose "Ask me later", or you are in an anonymous region): the report is anonymous. It carries the same screen, level, wave and timing information, but a coarse speed band instead of hardware model names, no account, and only the error lines from the log file (at most 4 KB). It is never written to your computer: it is sent once, and if that fails it is simply lost.

To keep the log anonymous, before any log text leaves your computer the game replaces your user folder name, and any path that contains your operating-system user name, with `<user>`.

### Exit reports

The prompt in section 2 appears only after your first battle. Anyone who closes the game before that — on the start screen, the title screen or partway through the prologue — leaves no gameplay log at all, so we would never learn where they stopped. To see that, when you close the game normally (the window's close button, or Quit in the menu) it sends **one exit report**.

An exit report is **always anonymous**, whatever you answered in section 2 and wherever you are: it never carries your Steam ID number, your hardware model names or any log text. It contains the date it was sent (the day only, no time), the screen you were on, the chapter, level, wave and that battle's settings if you were in a battle (difficulty, speech speed, the tower's maximum health and the level's article topic), the seconds since the battle started (if in a battle), the prologue step and part with its duration (if in the prologue), which screens you visited during this launch, how many battles you finished, how long the game had been running, the game version, your region as described in section 4, whether any save file existed when the game started (so we can tell first launches from returning ones), the seconds since your last key press or mouse click, the interface language, and if a question was open when you closed the game: how long it had been open, how many wrong keys you had pressed, how far the hint had been revealed, how many times the sentence was replayed automatically and how many times you replayed it yourself, and how many keys you had pressed in that question (**counts only**).

- **If you chose "No"** to sharing gameplay logs, no exit report is sent.
- **In every other case** it is sent once, at the moment the game closes. It is never written to your computer; if it cannot be sent within about two seconds, the game closes anyway and the report is simply lost.

## 4. Two different records, depending on where you are

Geolocation defaults are handled by checking your system's country registration directly through Steam.

### If you are in the EU, the EEA, the United Kingdom, Switzerland or mainland China

- **Complete Anonymity**: The generated log contains zero identifying markers—including Steam IDs, account numbers, system-generated tracking tokens, or device fingerprints. Connecting separate logs to a single user is technically impossible.
- **Data Obfuscation**: Timestamps are restricted exclusively to the calendar date, omitting precise times. Furthermore, country is recorded only for a handful of major markets: mainland China, the United Kingdom and Switzerland are each recorded as their own country, while every remaining EU or EEA country is grouped together under the single tag "EU-other".
- **No Hardware Fingerprint**: Model names are never sent. Your machine is described only by a coarse speed band (how long it takes to generate one standard line of speech), because model names combined with other fields could single a person out.
- **No Behavioral Timing**: Keystroke-level timing logs are entirely omitted. At a friction point the record still carries the audio playback profile, the clip start and stop times and the tactical state, but the keystroke timeline itself is dropped and replaced by counts and totals — replays used, how far into the word you were, seconds spent.
- **Regulatory Compliance**: Since these logs cannot be used to distinguish or trace any individual, they constitute completely anonymous data. Anonymous information falls outside the scope of the GDPR and the UK GDPR, and is expressly excluded from the definition of personal information under China's Personal Information Protection Law (PIPL, Article 4).

### If you are anywhere else

- **Account Tracking**: To monitor long-term player progression and accommodate potential data deletion requests, the system links your Steam account number (the numeric component of your Steam ID) to the session logs.
- **Hardware Details**: CPU and graphics adapter model names, core count and total system memory are included.
- **Detailed Input Logs**: For instances where you experience friction during gameplay, the comprehensive keystroke timeline outlined in Section 2 will be included in the report.

## 5. Why we collect it

To find out where the game confuses, frustrates or defeats players, and to fix those places in later updates. Specifically: which words are hard to hear, whether replays and hints actually help, whether the difficulty is set correctly, and whether pressure on the battlefield damages people's typing.

We do not use this data for advertising, we do not sell it, and we do not use it to make any decision about you as an individual.

## 6. Legal basis

Where this data is personal data, our legal basis is **your consent** (GDPR Article 6(1)(a)).
You may withdraw it at any time — see section 9.

## 7. Who else sees it

No one. The data goes directly to **Cloudflare, Inc.**, our data processor, and stays inside storage buckets locked to the **European Union** (Cloudflare R2 EU jurisdiction). Cloudflare just hosts the data; they don't look at what's inside. We don't partner with analytics companies, advertisers, or any other third parties, so your logs are never shared.

## 8. How long we keep it

Until two years after the game's full release, after which all records are deleted. If we decide to keep them longer, we will update this policy and say so here.

## 9. Your rights

- Request access: You may ask for a complete copy of the data we currently store regarding your sessions.
- Request erasure: You have the right to ask us to purge your collected logs.
- Revoke consent: Toggle off gameplay data sharing within the game's Settings menu. This immediately halts all transmissions and purges any pending data cached on your device, and it also stops crash reports and exit reports (section 3). Records that were already sent are covered by "Request erasure" above.
- File a formal complaint: If you believe your data has been mismanaged, you can contact your local regulatory body. This refers to your residency's national authority within the EU, the Information Commissioner's Office (ICO) in the UK, or — in mainland China — the department charged with personal information protection duties under Article 65 of the PIPL, a function coordinated nationally by the Cyberspace Administration of China.

**A Technical Caveat on Deletion/Access**: For users residing in the EU, EEA, UK, Switzerland or mainland China, our compliance with data minimization means your logs carry zero identifying metadata. Consequently, we are physically unable to isolate or verify "your" specific files to display or erase them. This is an engineered limitation of our strict anonymity protocol, not a refusal to cooperate.

**Global Requests**: If you are located outside these regions and wish to have your data erased, please email us from any address with your Steam account number or Steam profile URL. We will promptly delete all matching records.

## 10. Children

Distribution of this game is handled via Steam, which enforces its own account age minimums. Consequently, we do not intentionally gather personal information from minors. If you suspect that a child has inadvertently opted into our data collection, please notify us immediately so we can isolate and erase the corresponding logs.

## 11. Changes to this policy

To ensure complete accountability, this document is hosted in a public, version-controlled repository, allowing you to review all historical revisions and their respective dates of modification. Should our data collection practices change in the future, an updated policy will be published prior to those changes going into effect.

## 12. Complaints and questions

**support@ashenknightgames.com** — we answer every message about data.

---

*This English version is the authoritative text. Translations are provided for convenience;
if they conflict, this version applies.*
