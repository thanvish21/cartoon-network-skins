# Cartoon Network Hermes Skins

Custom skins (visual themes) for the [Hermes](https://github.com/NousResearch/hermes-agent) CLI agent, themed after Cartoon Network shows — from Ben 10 to Roll No. 21, Powerpuff Girls to Toonami classics, and everything in between.

Skins control the **visual presentation** of Hermes: banner colors, spinner faces/verbs, response-box labels, branding text, tool activity prefix, and ASCII art banners. They don't affect personality or behavior — just how things look.

**167 skins** — every one defines the full 28-color schema, a themed spinner, branding with show-flavored welcome/goodbye lines, a colored ASCII logo, a **unique hand-drawn hero icon themed to the show** (Omnitrix, bat, skull, dragon ball, paw, spiral, portal…), show-specific skills, and a rendered banner screenshot (see `screenshots/`).

Screenshots are rendered straight from each skin's YAML — palette, ASCII logo, hero art and branding — via `make_screenshots.py` (headless Chromium), so what you see is what the skin looks like.

## Quick Start

1. Browse the `skins/` directory and pick one you like
2. Copy the `.yaml` file to `~/.hermes/skins/`
3. Activate it:

```bash
# Session-only
/skin ben-10
# Permanent (add to ~/.hermes/config.yaml)
display:
  skin: ben-10
```

Missing values inherit from the default skin, so partial skins work too — but these all define the complete schema, so they look right out of the box.

## Available Skins

### Ben 10 Universe

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Ben 10** | Classic Omnitrix series — dial in a hero and save the world. | [`ben-10.yaml`](skins/ben-10.yaml) | <img src="screenshots/ben-10.png" width="180" alt="Ben 10 skin"> |
| **Ben 10: Alien Force** | Teen Ben leads a team against the Highbreed invasion. | [`ben-10-alien-force.yaml`](skins/ben-10-alien-force.yaml) | <img src="screenshots/ben-10-alien-force.png" width="180" alt="Ben 10: Alien Force skin"> |
| **Ben 10: Ultimate Alien** | The Ultimatrix era — every transformation, one step further. | [`ben-10-ultimate-alien.yaml`](skins/ben-10-ultimate-alien.yaml) | <img src="screenshots/ben-10-ultimate-alien.png" width="180" alt="Ben 10: Ultimate Alien skin"> |
| **Ben 10: Omniverse** | New Omnitrix, new universe, same hero time. | [`ben-10-omniverse.yaml`](skins/ben-10-omniverse.yaml) | <img src="screenshots/ben-10-omniverse.png" width="180" alt="Ben 10: Omniverse skin"> |
| **Ben 10 (2016)** | The reboot — Ben, Gwen and Max on the road with the Omnitrix. | [`ben-10-2016.yaml`](skins/ben-10-2016.yaml) | <img src="screenshots/ben-10-2016.png" width="180" alt="Ben 10 (2016) skin"> |
| **Generator Rex** | Nanite-built machines and EVO battles from the Ben 10 universe. | [`generator-rex.yaml`](skins/generator-rex.yaml) | <img src="screenshots/generator-rex.png" width="180" alt="Generator Rex skin"> |

### Cartoon Cartoons & Classics

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **The Powerpuff Girls** | Sugar, spice and everything nice — Townsville's tiny protectors. | [`powerpuff-girls.yaml`](skins/powerpuff-girls.yaml) | <img src="screenshots/powerpuff-girls.png" width="180" alt="The Powerpuff Girls skin"> |
| **The Powerpuff Girls (2016)** | The reboot — same trio, brighter neon and new baddies. | [`powerpuff-girls-2016.yaml`](skins/powerpuff-girls-2016.yaml) | <img src="screenshots/powerpuff-girls-2016.png" width="180" alt="The Powerpuff Girls (2016) skin"> |
| **Dexter's Laboratory** | The boy genius and his secret lab full of inventions. | [`dexter-laboratory.yaml`](skins/dexter-laboratory.yaml) | <img src="screenshots/dexter-laboratory.png" width="180" alt="Dexter's Laboratory skin"> |
| **Johnny Bravo** | The muscle-bound, hair-combing ladies' man of Aron City. | [`johnny-bravo.yaml`](skins/johnny-bravo.yaml) | <img src="screenshots/johnny-bravo.png" width="180" alt="Johnny Bravo skin"> |
| **Courage the Cowardly Dog** | A scaredy-cat dog protecting his owners in Nowhere. | [`courage-the-cowardly-dog.yaml`](skins/courage-the-cowardly-dog.yaml) | <img src="screenshots/courage-the-cowardly-dog.png" width="180" alt="Courage the Cowardly Dog skin"> |
| **Ed, Edd n Eddy** | Three friends, endless scams and one huge jawbreaker. | [`ed-edd-n-eddy.yaml`](skins/ed-edd-n-eddy.yaml) | <img src="screenshots/ed-edd-n-eddy.png" width="180" alt="Ed, Edd n Eddy skin"> |
| **Codename: Kids Next Door** | Five kids, a treehouse and a mission to fight adult tyranny. | [`kids-next-door.yaml`](skins/kids-next-door.yaml) | <img src="screenshots/kids-next-door.png" width="180" alt="Codename: Kids Next Door skin"> |
| **Foster's Home for Imaginary Friends** | A mansion full of imaginary friends waiting for adoption. | [`fosters-home.yaml`](skins/fosters-home.yaml) | <img src="screenshots/fosters-home.png" width="180" alt="Foster's Home for Imaginary Friends skin"> |
| **The Grim Adventures of Billy & Mandy** | Grim, Billy and Mandy — the weirdest trio this side of Endsville. | [`grim-adventures-of-billy-mandy.yaml`](skins/grim-adventures-of-billy-mandy.yaml) | <img src="screenshots/grim-adventures-of-billy-mandy.png" width="180" alt="The Grim Adventures of Billy & Mandy skin"> |
| **Samurai Jack** | A samurai trapped in a future ruled by the demon Aku. | [`samurai-jack.yaml`](skins/samurai-jack.yaml) | <img src="screenshots/samurai-jack.png" width="180" alt="Samurai Jack skin"> |
| **Cow and Chicken** | The adventures of a cow and her chicken brother. | [`cow-and-chicken.yaml`](skins/cow-and-chicken.yaml) | <img src="screenshots/cow-and-chicken.png" width="180" alt="Cow and Chicken skin"> |
| **I Am Weasel** | I.M. Weasel, the brilliant one — and I.R. Baboon, his rival. | [`i-am-weasel.yaml`](skins/i-am-weasel.yaml) | <img src="screenshots/i-am-weasel.png" width="180" alt="I Am Weasel skin"> |
| **2 Stupid Dogs** | Little Dog and Big Dog — the two dumbest, happiest dogs around. | [`2-stupid-dogs.yaml`](skins/2-stupid-dogs.yaml) | <img src="screenshots/2-stupid-dogs.png" width="180" alt="2 Stupid Dogs skin"> |
| **Whatever Happened to Robot Jones?** | A robot kid navigating middle school in a retro-future. | [`robot-jones.yaml`](skins/robot-jones.yaml) | <img src="screenshots/robot-jones.png" width="180" alt="Whatever Happened to Robot Jones? skin"> |
| **Mike, Lu & Og** | A city girl, a genius and a native boy on a tropical island. | [`mike-lu-og.yaml`](skins/mike-lu-og.yaml) | <img src="screenshots/mike-lu-og.png" width="180" alt="Mike, Lu & Og skin"> |
| **Sheep in the Big City** | An escaped military sheep living in the big city. | [`sheep-in-the-big-city.yaml`](skins/sheep-in-the-big-city.yaml) | <img src="screenshots/sheep-in-the-big-city.png" width="180" alt="Sheep in the Big City skin"> |
| **The Cramp Twins** | Identical twin brothers with opposite personalities. | [`the-cramp-twins.yaml`](skins/the-cramp-twins.yaml) | <img src="screenshots/the-cramp-twins.png" width="180" alt="The Cramp Twins skin"> |
| **Camp Lazlo** | Lazlo the bean scout monkey and the campers of Camp Kidney. | [`camp-lazlo.yaml`](skins/camp-lazlo.yaml) | <img src="screenshots/camp-lazlo.png" width="180" alt="Camp Lazlo skin"> |
| **My Gym Partner's a Monkey** | A boy transferred to a school for animals. | [`my-gym-partner-is-a-monkey.yaml`](skins/my-gym-partner-is-a-monkey.yaml) | <img src="screenshots/my-gym-partner-is-a-monkey.png" width="180" alt="My Gym Partner's a Monkey skin"> |
| **Squirrel Boy** | A boy and his loud, squirrel best friend. | [`squirrel-boy.yaml`](skins/squirrel-boy.yaml) | <img src="screenshots/squirrel-boy.png" width="180" alt="Squirrel Boy skin"> |
| **Hi Hi Puffy AmiYumi** | The real-life rock duo as cartoon adventures. | [`hi-hi-puffy-amiyumi.yaml`](skins/hi-hi-puffy-amiyumi.yaml) | <img src="screenshots/hi-hi-puffy-amiyumi.png" width="180" alt="Hi Hi Puffy AmiYumi skin"> |
| **The Life and Times of Juniper Lee** | An 11-year-old secretly protecting the world from monsters. | [`juniper-lee.yaml`](skins/juniper-lee.yaml) | <img src="screenshots/juniper-lee.png" width="180" alt="The Life and Times of Juniper Lee skin"> |
| **Class of 3000** | Andre 3000 teaches music at a school in Atlanta. | [`class-of-3000.yaml`](skins/class-of-3000.yaml) | <img src="screenshots/class-of-3000.png" width="180" alt="Class of 3000 skin"> |
| **Mucha Lucha!** | Masked luchadores wrestling for honor at the International School of Lucha. | [`mucha-lucha.yaml`](skins/mucha-lucha.yaml) | <img src="screenshots/mucha-lucha.png" width="180" alt="Mucha Lucha! skin"> |
| **The Problem Solverz** | Neon-soaked adventures with Alfe, Robo and Horace. | [`the-problem-solverz.yaml`](skins/the-problem-solverz.yaml) | <img src="screenshots/the-problem-solverz.png" width="180" alt="The Problem Solverz skin"> |
| **Out of Jimmy's Head** | Live-action and cartoon — whatever Jimmy imagines, gets out. | [`out-of-jimmys-head.yaml`](skins/out-of-jimmys-head.yaml) | <img src="screenshots/out-of-jimmys-head.png" width="180" alt="Out of Jimmy's Head skin"> |
| **Chowder** | An apprentice chef with a big appetite and a bigger imagination. | [`chowder.yaml`](skins/chowder.yaml) | <img src="screenshots/chowder.png" width="180" alt="Chowder skin"> |
| **The Marvelous Misadventures of Flapjack** | A boy and a pirate captain searching for Candied Island. | [`flapjack.yaml`](skins/flapjack.yaml) | <img src="screenshots/flapjack.png" width="180" alt="The Marvelous Misadventures of Flapjack skin"> |
| **Total Drama** | Reality TV satire — 22 campers, one island, zero mercy. | [`total-drama.yaml`](skins/total-drama.yaml) | <img src="screenshots/total-drama.png" width="180" alt="Total Drama skin"> |
| **Total DramaRama** | The Total Drama cast as chaotic toddlers. | [`total-dramarama.yaml`](skins/total-dramarama.yaml) | <img src="screenshots/total-dramarama.png" width="180" alt="Total DramaRama skin"> |
| **6teen** | Six teens working and hanging out at the Galleria mall. | [`6teen.yaml`](skins/6teen.yaml) | <img src="screenshots/6teen.png" width="180" alt="6teen skin"> |
| **Stoked** | Six teens working a summer at a surf resort. | [`stoked.yaml`](skins/stoked.yaml) | <img src="screenshots/stoked.png" width="180" alt="Stoked skin"> |
| **Robotboy** | A top-secret battle robot living with a normal family. | [`robotboy.yaml`](skins/robotboy.yaml) | <img src="screenshots/robotboy.png" width="180" alt="Robotboy skin"> |
| **Megas XLR** | A giant robot from the future, a slacker driver and a mechanic. | [`megas-xlr.yaml`](skins/megas-xlr.yaml) | <img src="screenshots/megas-xlr.png" width="180" alt="Megas XLR skin"> |
| **Xiaolin Showdown** | Monk warriors collecting Shen Gong Wu artifacts. | [`xiaolin-showdown.yaml`](skins/xiaolin-showdown.yaml) | <img src="screenshots/xiaolin-showdown.png" width="180" alt="Xiaolin Showdown skin"> |
| **The Secret Saturdays** | A cryptozoologist family hunting legendary creatures. | [`secret-saturdays.yaml`](skins/secret-saturdays.yaml) | <img src="screenshots/secret-saturdays.png" width="180" alt="The Secret Saturdays skin"> |
| **Sym-Bionic Titan** | Three alien teens pilot a giant mech to defend Earth. | [`sym-bionic-titan.yaml`](skins/sym-bionic-titan.yaml) | <img src="screenshots/sym-bionic-titan.png" width="180" alt="Sym-Bionic Titan skin"> |
| **Hero: 108** | Hidden Valley's secret animal army faces the HighRollers. | [`hero-108.yaml`](skins/hero-108.yaml) | <img src="screenshots/hero-108.png" width="180" alt="Hero: 108 skin"> |
| **Chop Socky Chooks** | Three kung-fu chickens defending their fish-and-chip shop. | [`chop-socky-chooks.yaml`](skins/chop-socky-chooks.yaml) | <img src="screenshots/chop-socky-chooks.png" width="180" alt="Chop Socky Chooks skin"> |
| **Skatoony** | Skateboarding quiz show — answer or wipe out! | [`skatoony.yaml`](skins/skatoony.yaml) | <img src="screenshots/skatoony.png" width="180" alt="Skatoony skin"> |
| **Hot Wheels Battle Force 5** | Racing cars with weapons, defending Earth from the Sark. | [`hot-wheels-battle-force-5.yaml`](skins/hot-wheels-battle-force-5.yaml) | <img src="screenshots/hot-wheels-battle-force-5.png" width="180" alt="Hot Wheels Battle Force 5 skin"> |
| **Monster Beach** | Surfing monsters living at the graveyard shore. | [`monster-beach.yaml`](skins/monster-beach.yaml) | <img src="screenshots/monster-beach.png" width="180" alt="Monster Beach skin"> |
| **Duck Dodgers** | Daffy Duck as the 24th-and-a-half-century space hero. | [`ducks-dodgers.yaml`](skins/ducks-dodgers.yaml) | <img src="screenshots/ducks-dodgers.png" width="180" alt="Duck Dodgers skin"> |
| **Loonatics Unleashed** | Futuristic descendants of the Looney Tunes saving Metropolis. | [`loonatics-unleashed.yaml`](skins/loonatics-unleashed.yaml) | <img src="screenshots/loonatics-unleashed.png" width="180" alt="Loonatics Unleashed skin"> |
| **Baby Looney Tunes** | The classic characters as toddlers in daycare. | [`baby-looney-tunes.yaml`](skins/baby-looney-tunes.yaml) | <img src="screenshots/baby-looney-tunes.png" width="180" alt="Baby Looney Tunes skin"> |
| **Krypto the Superdog** | Superman's dog protecting Metropolis as a family pet. | [`krypto-superdog.yaml`](skins/krypto-superdog.yaml) | <img src="screenshots/krypto-superdog.png" width="180" alt="Krypto the Superdog skin"> |

### Modern Cartoon Network

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Adventure Time** | Finn and Jake's mathematical quests across the Land of Ooo. | [`adventure-time.yaml`](skins/adventure-time.yaml) | <img src="screenshots/adventure-time.png" width="180" alt="Adventure Time skin"> |
| **Regular Show** | Mordecai and Rigby's very regular, very weird park jobs. | [`regular-show.yaml`](skins/regular-show.yaml) | <img src="screenshots/regular-show.png" width="180" alt="Regular Show skin"> |
| **The Amazing World of Gumball** | A blue cat and a goldfish navigating Elmore's chaos. | [`the-amazing-world-of-gumball.yaml`](skins/the-amazing-world-of-gumball.yaml) | <img src="screenshots/the-amazing-world-of-gumball.png" width="180" alt="The Amazing World of Gumball skin"> |
| **Steven Universe** | A half-gem boy learning to protect Beach City with the Crystal Gems. | [`steven-universe.yaml`](skins/steven-universe.yaml) | <img src="screenshots/steven-universe.png" width="180" alt="Steven Universe skin"> |
| **We Bare Bears** | Grizz, Panda and Ice Bear trying to fit in with humans. | [`we-bare-bears.yaml`](skins/we-bare-bears.yaml) | <img src="screenshots/we-bare-bears.png" width="180" alt="We Bare Bears skin"> |
| **We Baby Bears** | The baby bears' adventures through magical portals. | [`we-baby-bears.yaml`](skins/we-baby-bears.yaml) | <img src="screenshots/we-baby-bears.png" width="180" alt="We Baby Bears skin"> |
| **Uncle Grandpa** | Everyone's magical uncle and grandpa who only exists to help. | [`uncle-grandpa.yaml`](skins/uncle-grandpa.yaml) | <img src="screenshots/uncle-grandpa.png" width="180" alt="Uncle Grandpa skin"> |
| **Clarence** | A relentlessly sunny kid and his friends in Aberdale. | [`clarence.yaml`](skins/clarence.yaml) | <img src="screenshots/clarence.png" width="180" alt="Clarence skin"> |
| **Craig of the Creek** | Craig and his crew exploring the kid-ruled creek. | [`craig-of-the-creek.yaml`](skins/craig-of-the-creek.yaml) | <img src="screenshots/craig-of-the-creek.png" width="180" alt="Craig of the Creek skin"> |
| **OK K.O.! Let's Be Heroes** | K.O. trains to be a hero at Lakewood Plaza Turbo. | [`ok-ko.yaml`](skins/ok-ko.yaml) | <img src="screenshots/ok-ko.png" width="180" alt="OK K.O.! Let's Be Heroes skin"> |
| **Infinity Train** | Passengers ride an endless train solving their personal issues. | [`infinity-train.yaml`](skins/infinity-train.yaml) | <img src="screenshots/infinity-train.png" width="180" alt="Infinity Train skin"> |
| **Apple & Onion** | Two food friends chasing their dreams in the big city. | [`apple-onion.yaml`](skins/apple-onion.yaml) | <img src="screenshots/apple-onion.png" width="180" alt="Apple & Onion skin"> |
| **Victor and Valentino** | Two brothers exploring a Mexican folklore town. | [`victor-valentino.yaml`](skins/victor-valentino.yaml) | <img src="screenshots/victor-valentino.png" width="180" alt="Victor and Valentino skin"> |
| **Mao Mao: Heroes of Pure Heart** | A hot-tempered sheriff cat defending Pure Heart Valley. | [`mao-mao.yaml`](skins/mao-mao.yaml) | <img src="screenshots/mao-mao.png" width="180" alt="Mao Mao: Heroes of Pure Heart skin"> |
| **Summer Camp Island** | A magical summer camp where nothing is quite normal. | [`summer-camp-island.yaml`](skins/summer-camp-island.yaml) | <img src="screenshots/summer-camp-island.png" width="180" alt="Summer Camp Island skin"> |
| **Elliott from Earth** | A boy, his mom and a dinosaur stranded on Earth. | [`elliott-from-earth.yaml`](skins/elliott-from-earth.yaml) | <img src="screenshots/elliott-from-earth.png" width="180" alt="Elliott from Earth skin"> |
| **Mighty Magiswords** | Prohyas and Vambre collect magical swords for quests. | [`mighty-magiswords.yaml`](skins/mighty-magiswords.yaml) | <img src="screenshots/mighty-magiswords.png" width="180" alt="Mighty Magiswords skin"> |
| **The High Fructose Adventures of Annoying Orange** | The obnoxious fruit that never stops talking. | [`annoying-orange.yaml`](skins/annoying-orange.yaml) | <img src="screenshots/annoying-orange.png" width="180" alt="The High Fructose Adventures of Annoying Orange skin"> |
| **Teen Titans Go!** | The Titans' silly, snack-fueled side adventures. | [`teen-titans-go.yaml`](skins/teen-titans-go.yaml) | <img src="screenshots/teen-titans-go.png" width="180" alt="Teen Titans Go! skin"> |
| **Jade Armor** | A teen girl discovers a legendary jade armor. | [`jade-armor.yaml`](skins/jade-armor.yaml) | <img src="screenshots/jade-armor.png" width="180" alt="Jade Armor skin"> |
| **Unikitty** | The LEGO princess of rage and happiness in Unikittyland. | [`unikitty.yaml`](skins/unikitty.yaml) | <img src="screenshots/unikitty.png" width="180" alt="Unikitty skin"> |
| **Mixels** | Mix and match creatures from the Nixel-infested Mixel world. | [`mixels.yaml`](skins/mixels.yaml) | <img src="screenshots/mixels.png" width="180" alt="Mixels skin"> |
| **ThunderCats Roar** | The goofy 2019 reboot of the classic cat heroes. | [`thundercats-roar.yaml`](skins/thundercats-roar.yaml) | <img src="screenshots/thundercats-roar.png" width="180" alt="ThunderCats Roar skin"> |
| **DreamWorks Dragons** | Hiccup and Toothless' adventures from the Dragon franchise. | [`dreamworks-dragons.yaml`](skins/dreamworks-dragons.yaml) | <img src="screenshots/dreamworks-dragons.png" width="180" alt="DreamWorks Dragons skin"> |

### DC Super Heroes

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Teen Titans** | The classic Titans — Robin, Starfire, Raven, Cyborg and Beast Boy. | [`teen-titans.yaml`](skins/teen-titans.yaml) | <img src="screenshots/teen-titans.png" width="180" alt="Teen Titans skin"> |
| **Justice League** | Earth's mightiest heroes united as one team. | [`justice-league.yaml`](skins/justice-league.yaml) | <img src="screenshots/justice-league.png" width="180" alt="Justice League skin"> |
| **Justice League Unlimited** | The expanded league with dozens of heroes in action. | [`justice-league-unlimited.yaml`](skins/justice-league-unlimited.yaml) | <img src="screenshots/justice-league-unlimited.png" width="180" alt="Justice League Unlimited skin"> |
| **Batman: The Animated Series** | The Dark Knight of Gotham in the definitive animated take. | [`batman-tas.yaml`](skins/batman-tas.yaml) | <img src="screenshots/batman-tas.png" width="180" alt="Batman: The Animated Series skin"> |
| **Batman Beyond** | A teenager inherits the Batsuit in Neo-Gotham. | [`batman-beyond.yaml`](skins/batman-beyond.yaml) | <img src="screenshots/batman-beyond.png" width="180" alt="Batman Beyond skin"> |
| **Static Shock** | Virgil Hawkins — the electric superhero of Dakota. | [`static-shock.yaml`](skins/static-shock.yaml) | <img src="screenshots/static-shock.png" width="180" alt="Static Shock skin"> |
| **The Zeta Project** | A prototype spy robot trying to prove he's not a weapon. | [`zeta-project.yaml`](skins/zeta-project.yaml) | <img src="screenshots/zeta-project.png" width="180" alt="The Zeta Project skin"> |
| **Young Justice** | The teen sidekicks operating as a covert team. | [`young-justice.yaml`](skins/young-justice.yaml) | <img src="screenshots/young-justice.png" width="180" alt="Young Justice skin"> |
| **Green Lantern: The Animated Series** | Hal Jordan and Kilowog patrolling the universe. | [`green-lantern-tas.yaml`](skins/green-lantern-tas.yaml) | <img src="screenshots/green-lantern-tas.png" width="180" alt="Green Lantern: The Animated Series skin"> |
| **Beware the Batman** | The 2013 Batman series focused on Detective Gordon and Katana. | [`beware-the-batman.yaml`](skins/beware-the-batman.yaml) | <img src="screenshots/beware-the-batman.png" width="180" alt="Beware the Batman skin"> |
| **Justice League Action** | Fast-paced, fun-sized league adventures. | [`justice-league-action.yaml`](skins/justice-league-action.yaml) | <img src="screenshots/justice-league-action.png" width="180" alt="Justice League Action skin"> |
| **DC Super Hero Girls** | Super-powered teens balancing heroics and high school. | [`dc-super-hero-girls.yaml`](skins/dc-super-hero-girls.yaml) | <img src="screenshots/dc-super-hero-girls.png" width="180" alt="DC Super Hero Girls skin"> |
| **Batman: The Brave and the Bold** | Batman teaming up with heroes across the DC universe. | [`batman-brave-bold.yaml`](skins/batman-brave-bold.yaml) | <img src="screenshots/batman-brave-bold.png" width="180" alt="Batman: The Brave and the Bold skin"> |

### Star Wars & LEGO

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Star Wars: The Clone Wars** | Anakin, Obi-Wan and the clones in the Clone Wars era. | [`star-wars-clone-wars.yaml`](skins/star-wars-clone-wars.yaml) | <img src="screenshots/star-wars-clone-wars.png" width="180" alt="Star Wars: The Clone Wars skin"> |
| **Ninjago: Masters of Spinjitzu** | Elemental ninja protect Ninjago from the forces of darkness. | [`ninjago.yaml`](skins/ninjago.yaml) | <img src="screenshots/ninjago.png" width="180" alt="Ninjago: Masters of Spinjitzu skin"> |
| **LEGO Monkie Kid** | MK wields the Monkey King's staff against demons. | [`lego-monkie-kid.yaml`](skins/lego-monkie-kid.yaml) | <img src="screenshots/lego-monkie-kid.png" width="180" alt="LEGO Monkie Kid skin"> |
| **LEGO City Adventures** | Everyday heroes of LEGO City — cops, firefighters and more. | [`lego-city-adventures.yaml`](skins/lego-city-adventures.yaml) | <img src="screenshots/lego-city-adventures.png" width="180" alt="LEGO City Adventures skin"> |
| **ThunderCats (2011)** | Lion-O and the ThunderCats rebuild after Thundera's fall. | [`thundercats-2011.yaml`](skins/thundercats-2011.yaml) | <img src="screenshots/thundercats-2011.png" width="180" alt="ThunderCats (2011) skin"> |

### Toonami & Action

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Toonami** | The legendary action block — TOM's late-night anime lineup. | [`toonami.yaml`](skins/toonami.yaml) | <img src="screenshots/toonami.png" width="180" alt="Toonami skin"> |
| **Dragon Ball Z** | Goku and the Z-Fighters defending Earth from planet-level threats. | [`dragon-ball-z.yaml`](skins/dragon-ball-z.yaml) | <img src="screenshots/dragon-ball-z.png" width="180" alt="Dragon Ball Z skin"> |
| **Dragon Ball GT** | Goku shrunk to a kid, searching the Black Star Dragon Balls. | [`dragon-ball-gt.yaml`](skins/dragon-ball-gt.yaml) | <img src="screenshots/dragon-ball-gt.png" width="180" alt="Dragon Ball GT skin"> |
| **Dragon Ball Super** | Gods of Destruction, tournaments and Ultra Instinct. | [`dragon-ball-super.yaml`](skins/dragon-ball-super.yaml) | <img src="screenshots/dragon-ball-super.png" width="180" alt="Dragon Ball Super skin"> |
| **Naruto** | A loud ninja with a dream of becoming Hokage. | [`naruto.yaml`](skins/naruto.yaml) | <img src="screenshots/naruto.png" width="180" alt="Naruto skin"> |
| **Naruto Shippuden** | Naruto's older, darker journey to bring Sasuke home. | [`naruto-shippuden.yaml`](skins/naruto-shippuden.yaml) | <img src="screenshots/naruto-shippuden.png" width="180" alt="Naruto Shippuden skin"> |
| **One Piece** | Monkey D. Luffy's quest for the One Piece and the Pirate King title. | [`one-piece.yaml`](skins/one-piece.yaml) | <img src="screenshots/one-piece.png" width="180" alt="One Piece skin"> |
| **Bleach** | Ichigo Kurosaki, the substitute Soul Reaper. | [`bleach.yaml`](skins/bleach.yaml) | <img src="screenshots/bleach.png" width="180" alt="Bleach skin"> |
| **Cowboy Bebop** | Bounty hunters in space, jazz in the background. | [`cowboy-bebop.yaml`](skins/cowboy-bebop.yaml) | <img src="screenshots/cowboy-bebop.png" width="180" alt="Cowboy Bebop skin"> |
| **Samurai Champloo** | Hip-hop samurai road trip across Edo Japan. | [`samurai-champloo.yaml`](skins/samurai-champloo.yaml) | <img src="screenshots/samurai-champloo.png" width="180" alt="Samurai Champloo skin"> |
| **Eureka Seven** | Renton pilots the Nirvash and rides the trapar waves. | [`eureka-seven.yaml`](skins/eureka-seven.yaml) | <img src="screenshots/eureka-seven.png" width="180" alt="Eureka Seven skin"> |
| **Inuyasha** | A half-demon and a schoolgirl hunting Shikon shards. | [`inuyasha.yaml`](skins/inuyasha.yaml) | <img src="screenshots/inuyasha.png" width="180" alt="Inuyasha skin"> |
| **Fullmetal Alchemist** | Two brothers and the law of equivalent exchange. | [`fullmetal-alchemist.yaml`](skins/fullmetal-alchemist.yaml) | <img src="screenshots/fullmetal-alchemist.png" width="180" alt="Fullmetal Alchemist skin"> |
| **Yu Yu Hakusho** | Spirit detective Yusuke fighting the demon world. | [`yu-yu-hakusho.yaml`](skins/yu-yu-hakusho.yaml) | <img src="screenshots/yu-yu-hakusho.png" width="180" alt="Yu Yu Hakusho skin"> |
| **Hunter x Hunter** | Gon and Killua take the Hunter Exam and master Nen. | [`hunter-x-hunter.yaml`](skins/hunter-x-hunter.yaml) | <img src="screenshots/hunter-x-hunter.png" width="180" alt="Hunter x Hunter skin"> |
| **Attack on Titan** | Humanity fights for survival against the Titans. | [`attack-on-titan.yaml`](skins/attack-on-titan.yaml) | <img src="screenshots/attack-on-titan.png" width="180" alt="Attack on Titan skin"> |
| **My Hero Academia** | Deku trains to become the greatest hero at UA. | [`my-hero-academia.yaml`](skins/my-hero-academia.yaml) | <img src="screenshots/my-hero-academia.png" width="180" alt="My Hero Academia skin"> |
| **JoJo's Bizarre Adventure** | Generations of Joestars and their Stands. | [`jojo-bizarre-adventure.yaml`](skins/jojo-bizarre-adventure.yaml) | <img src="screenshots/jojo-bizarre-adventure.png" width="180" alt="JoJo's Bizarre Adventure skin"> |
| **Mob Psycho 100** | A powerful psychic trying to live an ordinary life. | [`mob-psycho-100.yaml`](skins/mob-psycho-100.yaml) | <img src="screenshots/mob-psycho-100.png" width="180" alt="Mob Psycho 100 skin"> |
| **Demon Slayer** | Tanjiro's quest to cure his sister and slay demons. | [`demon-slayer.yaml`](skins/demon-slayer.yaml) | <img src="screenshots/demon-slayer.png" width="180" alt="Demon Slayer skin"> |
| **Sword Art Online** | Players trapped in a deadly VRMMO must clear the game. | [`sword-art-online.yaml`](skins/sword-art-online.yaml) | <img src="screenshots/sword-art-online.png" width="180" alt="Sword Art Online skin"> |
| **One Punch Man** | Saitama ends every fight with one punch. | [`one-punch-man.yaml`](skins/one-punch-man.yaml) | <img src="screenshots/one-punch-man.png" width="180" alt="One Punch Man skin"> |
| **Dr. Stone** | Senku rebuilds civilization from stone with science. | [`dr-stone.yaml`](skins/dr-stone.yaml) | <img src="screenshots/dr-stone.png" width="180" alt="Dr. Stone skin"> |
| **Fire Force** | Special fire brigades fighting Infernals with flames. | [`fire-force.yaml`](skins/fire-force.yaml) | <img src="screenshots/fire-force.png" width="180" alt="Fire Force skin"> |
| **Mobile Suit Gundam Wing** | Five Gundam pilots and their fight for the colonies. | [`gundam-wing.yaml`](skins/gundam-wing.yaml) | <img src="screenshots/gundam-wing.png" width="180" alt="Mobile Suit Gundam Wing skin"> |
| **Mobile Suit Gundam 00** | Celestial Being intervenes to end war with Gundams. | [`gundam-00.yaml`](skins/gundam-00.yaml) | <img src="screenshots/gundam-00.png" width="180" alt="Mobile Suit Gundam 00 skin"> |
| **Space Dandy** | The dandy guy in space, hunting rare aliens. | [`space-dandy.yaml`](skins/space-dandy.yaml) | <img src="screenshots/space-dandy.png" width="180" alt="Space Dandy skin"> |
| **FLCL** | The surreal coming-of-age story with guitars and robots. | [`flcl.yaml`](skins/flcl.yaml) | <img src="screenshots/flcl.png" width="180" alt="FLCL skin"> |
| **The Big O** | Roger Smith and the giant robot Big O in Paradigm City. | [`big-o.yaml`](skins/big-o.yaml) | <img src="screenshots/big-o.png" width="180" alt="The Big O skin"> |
| **Mobile Fighter G Gundam** | The Gundam Fight tournament decides Earth's fate. | [`g-gundam.yaml`](skins/g-gundam.yaml) | <img src="screenshots/g-gundam.png" width="180" alt="Mobile Fighter G Gundam skin"> |
| **Tenchi Muyo** | An ordinary guy with extraordinary space friends. | [`tenchi-muyo.yaml`](skins/tenchi-muyo.yaml) | <img src="screenshots/tenchi-muyo.png" width="180" alt="Tenchi Muyo skin"> |
| **Sailor Moon** | Usagi and the Sailor Guardians fight evil by moonlight. | [`sailor-moon.yaml`](skins/sailor-moon.yaml) | <img src="screenshots/sailor-moon.png" width="180" alt="Sailor Moon skin"> |
| **Zoids** | Mecha beasts battling across the planet Zi. | [`zoids.yaml`](skins/zoids.yaml) | <img src="screenshots/zoids.png" width="180" alt="Zoids skin"> |
| **Outlaw Star** | Gene Starwind and the search for the Galactic Leyline. | [`outlaw-star.yaml`](skins/outlaw-star.yaml) | <img src="screenshots/outlaw-star.png" width="180" alt="Outlaw Star skin"> |
| **Rurouni Kenshin** | A wandering swordsman protecting the Meiji era. | [`rurouni-kenshin.yaml`](skins/rurouni-kenshin.yaml) | <img src="screenshots/rurouni-kenshin.png" width="180" alt="Rurouni Kenshin skin"> |
| **Deadman Wonderland** | Ganta fights for survival in a deadly prison. | [`deadman-wonderland.yaml`](skins/deadman-wonderland.yaml) | <img src="screenshots/deadman-wonderland.png" width="180" alt="Deadman Wonderland skin"> |
| **Trigun** | Vash the Stampede — the pacifist gunslinger with a $$60 billion bounty. | [`trigun.yaml`](skins/trigun.yaml) | <img src="screenshots/trigun.png" width="180" alt="Trigun skin"> |
| **Bakugan** | Battle brawlers with cards that spring into creatures. | [`bakugan.yaml`](skins/bakugan.yaml) | <img src="screenshots/bakugan.png" width="180" alt="Bakugan skin"> |
| **Beyblade** | Spinning tops battle it out in the beystadium. | [`beyblade.yaml`](skins/beyblade.yaml) | <img src="screenshots/beyblade.png" width="180" alt="Beyblade skin"> |
| **Beyblade Burst** | The Burst era — beys that burst apart at high speed. | [`beyblade-burst.yaml`](skins/beyblade-burst.yaml) | <img src="screenshots/beyblade-burst.png" width="180" alt="Beyblade Burst skin"> |

### Adult Swim

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Rick and Morty** | A genius mad scientist and his grandson across dimensions. | [`rick-and-morty.yaml`](skins/rick-and-morty.yaml) | <img src="screenshots/rick-and-morty.png" width="180" alt="Rick and Morty skin"> |
| **Aqua Teen Hunger Force** | Master Shake, Frylock and Meatwad's bizarre suburban life. | [`aqua-teen-hunger-force.yaml`](skins/aqua-teen-hunger-force.yaml) | <img src="screenshots/aqua-teen-hunger-force.png" width="180" alt="Aqua Teen Hunger Force skin"> |
| **Robot Chicken** | Stop-motion sketch comedy with pop-culture mayhem. | [`robot-chicken.yaml`](skins/robot-chicken.yaml) | <img src="screenshots/robot-chicken.png" width="180" alt="Robot Chicken skin"> |
| **Space Ghost Coast to Coast** | A retired superhero hosts a talk show. | [`space-ghost-coast-to-coast.yaml`](skins/space-ghost-coast-to-coast.yaml) | <img src="screenshots/space-ghost-coast-to-coast.png" width="180" alt="Space Ghost Coast to Coast skin"> |
| **Harvey Birdman, Attorney at Law** | A superhero lawyer defending cartoon characters. | [`harvey-birdman.yaml`](skins/harvey-birdman.yaml) | <img src="screenshots/harvey-birdman.png" width="180" alt="Harvey Birdman, Attorney at Law skin"> |
| **Sealab 2021** | A dysfunctional underwater research station. | [`sealab-2021.yaml`](skins/sealab-2021.yaml) | <img src="screenshots/sealab-2021.png" width="180" alt="Sealab 2021 skin"> |
| **The Venture Bros.** | The Venture family — failed scientists and bodyguards. | [`venture-bros.yaml`](skins/venture-bros.yaml) | <img src="screenshots/venture-bros.png" width="180" alt="The Venture Bros. skin"> |
| **Metalocalypse** | The world's greatest death metal band, Dethklok. | [`metalocalypse.yaml`](skins/metalocalypse.yaml) | <img src="screenshots/metalocalypse.png" width="180" alt="Metalocalypse skin"> |
| **Squidbillies** | Squid-mountain-dwellers causing trouble in the backwoods. | [`squidbillies.yaml`](skins/squidbillies.yaml) | <img src="screenshots/squidbillies.png" width="180" alt="Squidbillies skin"> |

### Acquired & International

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Tom and Jerry** | The eternal cat-and-mouse chase that needs no intro. | [`tom-and-jerry.yaml`](skins/tom-and-jerry.yaml) | <img src="screenshots/tom-and-jerry.png" width="180" alt="Tom and Jerry skin"> |
| **Scooby-Doo** | Mystery Inc. and the Mystery Machine solving spooky cases. | [`scooby-doo.yaml`](skins/scooby-doo.yaml) | <img src="screenshots/scooby-doo.png" width="180" alt="Scooby-Doo skin"> |
| **What's New, Scooby-Doo?** | The 2000s Mystery Inc. — same gang, new mysteries. | [`whats-new-scooby-doo.yaml`](skins/whats-new-scooby-doo.yaml) | <img src="screenshots/whats-new-scooby-doo.png" width="180" alt="What's New, Scooby-Doo? skin"> |
| **Scooby-Doo! Mystery Incorporated** | The darker serialized Mystery Inc. mystery. | [`scooby-doo-mystery-incorporated.yaml`](skins/scooby-doo-mystery-incorporated.yaml) | <img src="screenshots/scooby-doo-mystery-incorporated.png" width="180" alt="Scooby-Doo! Mystery Incorporated skin"> |
| **Johnny Test** | A boy and his genius sisters' experiments. | [`johnny-test.yaml`](skins/johnny-test.yaml) | <img src="screenshots/johnny-test.png" width="180" alt="Johnny Test skin"> |
| **The Garfield Show** | The lasagna-loving cat and his friends. | [`garfield-show.yaml`](skins/garfield-show.yaml) | <img src="screenshots/garfield-show.png" width="180" alt="The Garfield Show skin"> |
| **Oggy and the Cockroaches** | A cat's quiet life ruined by three cockroaches. | [`oggy-cockroaches.yaml`](skins/oggy-cockroaches.yaml) | <img src="screenshots/oggy-cockroaches.png" width="180" alt="Oggy and the Cockroaches skin"> |
| **Zig & Sharko** | A hyena's endless attempts to catch a mermaid. | [`zig-sharko.yaml`](skins/zig-sharko.yaml) | <img src="screenshots/zig-sharko.png" width="180" alt="Zig & Sharko skin"> |
| **Grizzy and the Lemmings** | A bear vs. the lemmings in a national park cabin. | [`grizzy-lemmings.yaml`](skins/grizzy-lemmings.yaml) | <img src="screenshots/grizzy-lemmings.png" width="180" alt="Grizzy and the Lemmings skin"> |
| **Mr. Bean: The Animated Series** | The beloved bumbling everyman, animated. | [`mr-bean-animated.yaml`](skins/mr-bean-animated.yaml) | <img src="screenshots/mr-bean-animated.png" width="180" alt="Mr. Bean: The Animated Series skin"> |
| **Taffy** | A crafty cat and a dog in a mansion full of schemes. | [`taffy.yaml`](skins/taffy.yaml) | <img src="screenshots/taffy.png" width="180" alt="Taffy skin"> |
| **Angelo Rules** | A boy using elaborate plans to get what he wants. | [`angelo-rules.yaml`](skins/angelo-rules.yaml) | <img src="screenshots/angelo-rules.png" width="180" alt="Angelo Rules skin"> |
| **Transformers: Animated** | The Autobots as a repair crew in Detroit. | [`transformers-animated.yaml`](skins/transformers-animated.yaml) | <img src="screenshots/transformers-animated.png" width="180" alt="Transformers: Animated skin"> |
| **Code Lyoko** | Virtual warriors entering Lyoko to fight XANA. | [`code-lyoko.yaml`](skins/code-lyoko.yaml) | <img src="screenshots/code-lyoko.png" width="180" alt="Code Lyoko skin"> |
| **Mega Man: Fully Charged** | The blue bomber reborn for a new generation. | [`mega-man-fully-charged.yaml`](skins/mega-man-fully-charged.yaml) | <img src="screenshots/mega-man-fully-charged.png" width="180" alt="Mega Man: Fully Charged skin"> |

### Cartoon Network India

| Skin | Description | File | Screenshot |
|------|-------------|------|------------|
| **Roll No. 21** | Krishna, the mischievous kid who gets into magical trouble. | [`roll-no-21.yaml`](skins/roll-no-21.yaml) | <img src="screenshots/roll-no-21.png" width="180" alt="Roll No. 21 skin"> |
| **Pakdam Pakdai** | Cat vs. mouse in a wacky, fast-paced chase. | [`pakdam-pakdai.yaml`](skins/pakdam-pakdai.yaml) | <img src="screenshots/pakdam-pakdai.png" width="180" alt="Pakdam Pakdai skin"> |
| **Gattu Battu** | A boy and his faithful dog on everyday adventures. | [`gattu-battu.yaml`](skins/gattu-battu.yaml) | <img src="screenshots/gattu-battu.png" width="180" alt="Gattu Battu skin"> |
| **Rohan & Anisha** | A boy and his alien friend's city adventures. | [`rohan-anisha.yaml`](skins/rohan-anisha.yaml) | <img src="screenshots/rohan-anisha.png" width="180" alt="Rohan & Anisha skin"> |
| **Kumbh Karan** | The sleepy giant from the legends, now a lovable kid. | [`kumbh-karan.yaml`](skins/kumbh-karan.yaml) | <img src="screenshots/kumbh-karan.png" width="180" alt="Kumbh Karan skin"> |
| **Chumbak** | A magnet-powered kid attracting adventure. | [`chumbak.yaml`](skins/chumbak.yaml) | <img src="screenshots/chumbak.png" width="180" alt="Chumbak skin"> |
| **Viramputin** | A cartoonist's characters come to life in a wild town. | [`viramputin.yaml`](skins/viramputin.yaml) | <img src="screenshots/viramputin.png" width="180" alt="Viramputin skin"> |
| **Supa Strikas** | The world's best street football team. | [`supa-strikas.yaml`](skins/supa-strikas.yaml) | <img src="screenshots/supa-strikas.png" width="180" alt="Supa Strikas skin"> |
| **Lamput** | A blob of orange goo outsmarting two lab scientists. | [`lamput.yaml`](skins/lamput.yaml) | <img src="screenshots/lamput.png" width="180" alt="Lamput skin"> |

## Themes for Other AI Coding Tools

Every show also ships as a ready-to-use theme for Claude Code and OpenCode (same palette, ported from the Hermes skin).

### Claude Code

Each theme is a JSON file in `themes/claude-code/` with the official Claude Code format (`base: dark` + color token `overrides`). Install:

```bash
mkdir -p ~/.claude/themes
cp themes/claude-code/ben-10.json ~/.claude/themes/
claude   # then run /theme and pick 'Ben 10'
```

### OpenCode

Each theme is a JSON file in `themes/opencode/` following the official `theme.json` schema (dark/light pairs, markdown + syntax tokens). Install:

```bash
mkdir -p ~/.config/opencode/themes
cp themes/opencode/ben-10.json ~/.config/opencode/themes/
opencode   # then run /theme and pick 'Ben 10'
```

Regenerate them any time with `python3 generate_themes.py`.

### Freebuff

Freebuff is a terminal-based AI coding agent and does not expose a theme file format to customize — the pack's palettes still apply to whatever terminal you run it in (see the Hermes skin colors for the hex values).

## How Skins Work

Hermes loads skins from two locations (user skins take priority):

1. `~/.hermes/skins/<name>.yaml` (user custom)
2. Built-in skins hardcoded in `skin_engine.py`

The engine merges your skin on top of `default`, so partial skins work fine. Unknown skin names silently fall back to `default`.

## Creating Your Own

Drop a YAML file in `~/.hermes/skins/<name>.yaml`. The `name:` field inside must match the filename. See [SCHEMA.md](SCHEMA.md) for the complete list of configurable keys, or regenerate everything after editing the databases:

```bash
python3 generate_skins.py   # regenerate skins/ + docs + validate
python3 generate_skins.py --check   # validate existing skins/ only
```

## Disclaimer

This is a fan-made project. Cartoon Network, and all show names, characters and related properties are trademarks of their respective owners (Warner Bros. Discovery and others). This project is not affiliated with, endorsed by, or sponsored by Cartoon Network or Warner Bros. Discovery. The skin YAML files themselves are original creations released under the MIT license.

## License

[MIT](LICENSE)
