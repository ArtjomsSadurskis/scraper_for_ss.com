Artem Šadurski projekts (211REC086) Lietojumprogrammatūras automatizēšanas rīki(1) (DIP225)
1. kurss RDBF0 Automātika un datorzinātnes, 1. semestris 23/24-R

# Web skrāpēšanas skripts, izmantojot Selenium un Telegram integrāciju

Projekta mērķis Man patīk elektronika: audio, tālruņi, datoru daļas utt.
Latvijā lielākā tehnikas pirkšanas un pārdošanas platforma ir ss.com, otra lielākā ir facebook/marketplace (mēģināju to metāllūžņos, līdz sapratu lapu struktūru).
Atgriezīsimies pie ss.com, man jau 3-4 gadus ir ieradums meklēt interesantus sludinājumus dažādās sadaļās, gan retu elektroniku, gan vienkārši labus darījumus. ļoti bieži labas lotiņas pamana tikai pēc kāda laika un 100% varbūtības tās atrast.
Par to, cik paziņošanas sistēmas ss.com nav, es nolēmu, ka man ir nepieciešams automatizēt šo uzdevumu, palielinot efektivitāti un atbrīvojot sev aptuveni 2-3 stundas laika dienā, šajā laikā es varu kodēt vai nodarboties ar sportu. Ceru, ka šīs vietnes izvēles un darba ar to iemeslu esmu izskaidrojis.


Par kodu
Šis skripts izmanto Selenium, lai veiktu tīmekļa skrāpēšanu konkrētā ss.com vietnē, un iegūto informāciju nosūta uz Telegram tērzēšanu, izmantojot Telegram Bot API.


Python bibliotēkas, ko esmu izmantojis:

selenium: Izmanto, lai automatizētu tīmekļa pārlūkprogrammu. Jūsu kodā tas tiek izmantots, lai mijiedarbotos ar tīmekļa lapu, atverot lapu, noklikšķinot uz elementiem, iegūstot datus utt.

time: Izmanto, lai radītu laika aizkavēšanos, lai pārlūkprogrammai un lapai dotu laiku ielādēties un apstrādāt.

asyncio: Izmanto uzdevumu asinhronai apstrādei. Jūsu kods satur asinhrono funkciju main() un tās izpildei izmanto asyncio notikumu cilpu.

telegram: Paredzams, ka šī ir pielāgota bibliotēka darbam ar Telegram API. Jūs to izmantojat, lai sūtītu ziņojumus Telegram botam.

schedule: to izmanto, lai izveidotu un pārvaldītu uzdevumu grafiku. Jūsu kodā tas tiek izmantots, lai palaistu job() ik pēc 6 minūtēm.

webdriver.Chrome un webdriver.ChromeOptions: Selenium bibliotēkas daļa, kas ļauj pārvaldīt tīmekļa pārlūkprogrammu Chrome un definēt tās palaišanas opcijas.



## Priekšnosacījumi

- Python 3.x
- Instalējiet nepieciešamās paketes, izpildot šādu komandu:
  ````bash
  pip install selenium python-telegram-bot schedule


Lejupielādējiet ChromeDriver izpildāmo programmu un pārliecinieties, ka tā ir jūsu sistēmas PATH mainīgajā.

1.SOLIS

Pielāgošana

Lai izveidotu robotu, es izmantoju robotu https://t.me/BotFather.

1.Sākt darbu ar robotu, redzot komandu /start
2.Izvēlieties /newbot
3.Botam tiks piedāvāts izveidot sava bota (palīga) nosaukumu Manā gadījumā tas ir https://t.me/scraper_market_bot.
4.Pēc izveides jums tiks nosūtīts šis ziņojums:


Done! Congratulations on your new bot. You will find it at t.me/scraper_market_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8      <-------------------- šis ir jūsu telegram bot kods.

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api




5.Lai ziņojumi sasniegtu jūs instalēt bibliotēku, ja tā neeksistē, izmantojot komandu:

1.pip instalēt python-telegram-bot
2.telegram-send --configure

P.S konsolē jums būs jāievada žetons, ko jums nosūtīja https://t.me/BotFather.
3.6393465137:AAHN7u7UWD5yjyiik9COgwV9QbfTsJVtoU8 
4.Konsoles sadaļā tiks norādīta parole, kas jānosūta jūsu botam, lai tas sāktu darboties.
5.Ierakstiet botam komandu /start un ievadiet savu paroli. (Piemērs parole:01617)


P.S Ja manas instrukcijas jums nepalīdzēja, varat izmantot šo video: https://www.youtube.com/watch?v=-73hRicngD8&ab_channel=TheLookin.


2.SOLIS

Lai uzzinātu chat_id:

Meklēt telegram bot https://t.me/userinfobot.
2.Sākt tērzēšanu ar komandu /start
3.Tas nosūtīs jums ziņu ar visu jūsu informāciju:
Tavs vārds un uzvārds: @Urnickname
Id: 626358089 <----------- ir jūsu Id
Pirmais: Vārds
Uzvārds: Uzvārds
Lang: Eng



3.STEP Darbs ar kodu
Visā kodā centos atstāt komentārus, lai būtu skaidrs, ka to var pielāgot citiem serveriem, citām kategorijām utt.

1.Ievietojiet skripta tekstā savu Telegram Bot žetonu un tērzēšanas ID:

bot_token = 'your_token_bot' (jūsu_token_bot).
chat_id = 'your_chat_id'


2.Pielāgojiet skriptu atbilstoši savām tīmekļa skrāpēšanas prasībām.


Lietošana
Palaidiet skriptu, izmantojot šādu komandu:

python scrapska.py


Skripts tiks palaists periodiski (ik pēc 6 minūtēm, saskaņā ar grafiku) un nosūtīs iegūto informāciju uz norādīto Telegram tērzēšanu.



Skripta pārskats

Skripts inicializē Chrome WebDriver, izmantojot Selenium, lai mijiedarbotos ar vietni.
Tas navigē tīmekļa vietnē uz konkrētu lapu un iegūst informāciju.
Ja tiek atrasts elements ar noteiktu XPath, skripts uz tā noklikšķina.
Pēc tam iegūtā informācija tiek nosūtīta uz Telegram tērzēšanu.




!!!! Pirms skripta palaišanas pārliecinieties, ka ir instalētas nepieciešamās paketes un konfigurēti Telegram Bot API akreditācijas dati!!!!.