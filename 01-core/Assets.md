# Assets — Icons, Sounds & Decoder

Full tables originally from SiteGPT V11 §10 / §11 and Mailo Assets.md.  
All asset IDs below are **confirmed pre-uploaded** — never invent new ones.

## Icon Library (84 Lucide icons)

256×256 px, pure white, 2 px stroke, rounded caps.  
Use with `ImageLabel` / `ImageButton`:

```json
{
  "class": "ImageLabel",
  "globalid": "ic",
  "image": "rbxassetid://76297972789266",
  "image_id": "76297972789266",
  "image_color": "#adadad",
  "scale_type": "Fit",
  "background_transparency": "1",
  "size": "{0,24},{0,24}"
}
```

Sizes: `{0,16},{0,16}` inline · `{0,24},{0,24}` default · `{0,32},{0,32}` card.

| # | Name | Asset ID | Common uses |
|---|------|----------|-------------|
| 1 | house | 128490289676597 | Home, navbar brand |
| 2 | search | 76297972789266 | Search bar/button |
| 3 | user-round | 117017076630548 | Profile, account |
| 4 | settings | 123045282429289 | Settings, admin |
| 5 | mail | 114078871101444 | Contact, email |
| 6 | star | 73775766036081 | Ratings, featured |
| 7 | heart | 81821025513215 | Like, wishlist |
| 8 | arrow-left | 132053311021067 | Back |
| 9 | arrow-right | 86341424256591 | Next, CTA |
| 10 | plus | 128762341789893 | Add, create |
| 11 | x | 97241930499310 | Close, dismiss |
| 12 | pencil | 76098741870595 | Edit |
| 13 | trash | 106229864631841 | Delete |
| 14 | download | 111132539535750 | Download |
| 15 | upload | 92547022320190 | Upload |
| 16 | link | 128161995104832 | External link |
| 17 | info | 132978996034921 | Info, help |
| 18 | triangle-alert | 101044232164905 | Warning |
| 19 | grid-2x2 | 133463448364347 | Grid / menu |
| 20 | bell | 130734329855948 | Notifications |
| 21 | bell-off | 131313860737094 | Muted |
| 22 | menu | 84352806499655 | Hamburger |
| 23 | check | 99802726511524 | Success |
| 24 | chevron-down | 87080095544609 | Dropdown |
| 25 | chevron-up | 96573229929402 | Collapse |
| 26 | clock | 82968254856227 | Time |
| 27 | calendar | 123093358000872 | Date |
| 28 | eye | 88997485015923 | Show |
| 29 | eye-off | 139554241318642 | Hide |
| 30 | lock | 99601667182985 | Locked |
| 31 | lock-open | 128013412438498 | Unlocked |
| 32 | share-2 | 114039748228833 | Share |
| 33 | external-link | 122444800533384 | Outbound |
| 34 | copy | 130977740797889 | Copy |
| 35 | rotate-cw | 103831305015789 | Refresh |
| 36 | funnel | 91180148376757 | Filter |
| 37 | list-sort-ascending | 132178203048228 | Sort A→Z |
| 38 | list-sort-descending | 96229858716187 | Sort Z→A |
| 39 | arrow-up-right | 118136232094518 | External direction |
| 40 | loader | 100424218947821 | Loading |
| 41 | loader-circle | 81239384648948 | Spinner |
| 42 | ellipsis-vertical | 81626897936532 | Overflow vertical |
| 43 | ellipsis | 139825203386447 | Overflow horizontal |
| 44 | bookmark | 92628008144421 | Bookmark |
| 45 | message-circle | 74178575771264 | Chat / comments |
| 46 | volume-2 | 103516276905873 | Audio on |
| 47 | sun | 80788164629601 | Light mode |
| 48 | moon | 124700849271660 | Dark mode |
| 49 | zap | 98819316845453 | Premium / power |
| 50 | map | 92300540805299 | Maps |
| 51 | map-pin | 116471861153777 | Location |
| 52 | phone | 133427066456170 | Phone / support |
| 53 | folder | 93755286057513 | Files |
| 54 | shopping-bag | 110888789046931 | Store |
| 55 | store | 76740445213011 | Marketplace |
| 56 | users-round | 103128988356985 | Team |
| 57 | layers | 80429653768693 | Versions |
| 58 | layout-grid | 94828998904657 | Dashboard |
| 59 | wallet | 100717817674057 | Balance |
| 60 | megaphone | 105447664594265 | Announcements |
| 61 | image | 76478225596850 | Media placeholder |
| 62 | shopping-cart | 117074905498023 | Cart |
| 63 | send | 118501485251954 | Submit |
| 64 | shield-check | 116015031695975 | Verified |
| 65 | play | 100984531058540 | Play / demo |
| 66 | globe | 132473860015433 | Language / global |
| 67 | badge-check | 75364661852335 | Verified badge |
| 68 | list | 126181252830019 | List view |
| 69 | refresh-cw | 122404692422803 | Sync |
| 70 | save | 139830175443527 | Save |
| 71 | sliders-horizontal | 100952596126070 | Filters |
| 72 | trending-up | 117604461413371 | Growth |
| 73 | lightbulb | 114237527539643 | Idea |
| 74 | history | 132539284401125 | Recent |
| 75 | file | 119100927707815 | File |
| 76 | brain | 110674321553035 | AI |
| 77 | credit-card | 122689283993405 | Billing |
| 78 | shield | 132071632855830 | Privacy |
| 79 | minus | 137413491041285 | Remove |
| 80 | dot | 115463795068023 | Status / bullet |
| 81 | camera | 90172905139857 | Photo |
| 82 | package | 82366494295497 | Product |
| 83 | flame | 136802848902260 | Trending |
| 84 | ban | 134524065816559 | Blocked |

## Sound Library (8 UI sounds)

Play with action id `5` (one-shot) or `26` (looped). Capture the handle if you need to stop/volume later.

| # | Name | Asset ID | Use |
|---|------|----------|-----|
| 1 | click | 88442833509532 | Primary button / tap |
| 2 | hover | 107511012621133 | Mouse-enter tick |
| 3 | toggle | 94316899429786 | Switch / checkbox |
| 4 | success | 136211732441165 | Confirmation (~2 s) |
| 5 | error | 131661013076677 | Invalid / failed |
| 6 | notification | 131039887376992 | Incoming alert |
| 7 | send | 5485567028 | Form / message submit |
| 8 | transition | 119137729729534 | Page / view change |

## Decoder (long strings only)

Roblox’s filter can turn long text into `######`.  
**Do not encode ordinary copy.** Only use the decoder for genuinely long paragraphs.

Full character → code table + the exact importable decoder script live in **SiteGPT V11 §9**.  
Import the decoder as its own `"class":"script"` element, leave the target label’s `text` empty, then call `Run function (d)` on load and `Set text`.

Never invent encodings or run external tools to compute them — look up codes manually from the table.
