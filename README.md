# 🏙️ MTGA — Make [Your City] Great Again

> A citizen-driven, open-source civic complaint portal 
> built for Indian municipal corporations.
> Forked from Tambaram. Built for everywhere.

## 🚀 Live Demo
This page (inspired and modeled after a rudimentary, buggy and error-prone Voice of Tambaram that was rolled by corporation)

## 💡 Why this exists
Every Indian city has a civic portal. None of them work.
This one is built differently — by citizens, for citizens,
with officials firmly in the crosshairs.

## ⚡ What makes it different
- 🔴 **Corruption reporting built-in** — not an afterthought. officials beware
- 📍 **GPS + static map** stamped on every complaint
- 🖼️ **Shareable complaint image** — straight to WhatsApp/X
- 🔒 **IP stamping** including X-Forwarded-For (proxy/VPN aware)
- 🌐 **Bilingual** — English + regional language toggle
- 🗺️ **Ward map** sidebar built in
- 🐄 **No animal complaint categories** — by design. We believe strongly in cohabitation, live and let-live ideology.

## 🏷️ Whitelabel in 10 minutes
Edit `config.js`:
```json
{
  "city": "Your City",
  "corporation": "Your Corp Name",
  "slogan": "Make [City] Great Again",
  "hashtags": ["#MXGA", "#YourCorpName"],
  "languages": ["en", "ta"],
  "mapsApiKey": "YOUR_KEY_HERE",
  "zones": [...],
  "wards": [...]
}
```

## 🏛️ Deployed by
| City | Corporation | Link |
|------|------------|------|
| *Your city here* | | Submit a PR |

## 📣 How it works
Every complaint generates a shareable image card and gets 
posted to social media tagging the corporation — and sometimes 
@realDonaldTrump, because why not. 🙃

## License: MIT
