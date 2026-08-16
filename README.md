# Cartoon Network Hermes Skins

Custom skins (visual themes) for the [Hermes](https://github.com/NousResearch/hermes-agent) CLI agent, themed after Cartoon Network shows — from Ben 10 to Roll No. 21, Powerpuff Girls to Toonami classics, and everything in between.

Skins control the **visual presentation** of Hermes: banner colors, spinner faces/verbs, response-box labels, branding text, tool activity prefix, and ASCII art banners. They don't affect personality or behavior — just how things look.

**167 skins** — every one defines the full 28-color schema, a themed spinner, branding with show-flavored welcome/goodbye lines, a colored ASCII logo, and a hero panel.

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

| Skin | Description | File |
|------|-------------|------|
| **Ben 10** | Classic Omnitrix series — dial in a hero and save the world. | [`ben-10.yaml`](skins/ben-10.yaml) |
| **Ben 10: Alien Force** | Teen Ben leads a team against the Highbreed invasion. | [`ben-10-alien-force.yaml`](skins/ben-10-alien-force.yaml) |
| **Ben 10: Ultimate Alien** | The Ultimatrix era — every transformation, one step further. | [`ben-10-ultimate-alien.yaml`](skins/ben-10-ultimate-alien.yaml) |
| **Ben 10: Omniverse** | New Omnitrix, new universe, same hero time. | [`ben-10-omniverse.yaml`](skins/ben-10-omniverse.yaml) |
| **Ben 10 (2016)** | The reboot — Ben, Gwen and Max on the road with the Omnitrix. | [`ben-10-2016.yaml`](skins/ben-10-2016.yaml) |
| **Generator Rex** | Nanite-built machines and EVO battles from the Ben 10 universe. | [`generator-rex.yaml`](skins/generator-rex.yaml) |

### Cartoon Cartoons & Classics

| Skin | Description | File |
|------|-------------|------|
| **The Powerpuff Girls** | Sugar, spice and everything nice — Townsville's tiny protectors. | [`powerpuff-girls.yaml`](skins/powerpuff-girls.yaml) |
| **The Powerpuff Girls (2016)** | The reboot — same trio, brighter neon and new baddies. | [`powerpuff-girls-2016.yaml`](skins/powerpuff-girls-2016.yaml) |
| **Dexter's Laboratory** | The boy genius and his secret lab full of inventions. | [`dexter-laboratory.yaml`](skins/dexter-laboratory.yaml) |
| **Johnny Bravo** | The muscle-bound, hair-combing ladies' man of Aron City. | [`johnny-bravo.yaml`](skins/johnny-bravo.yaml) |
| **Courage the Cowardly Dog** | A scaredy-cat dog protecting his owners in Nowhere. | [`courage-the-cowardly-dog.yaml`](skins/courage-the-cowardly-dog.yaml) |
| **Ed, Edd n Eddy** | Three friends, endless scams and one huge jawbreaker. | [`ed-edd-n-eddy.yaml`](skins/ed-edd-n-eddy.yaml) |
| **Codename: Kids Next Door** | Five kids, a treehouse and a mission to fight adult tyranny. | [`kids-next-door.yaml`](skins/kids-next-door.yaml) |
| **Foster's Home for Imaginary Friends** | A mansion full of imaginary friends waiting for adoption. | [`fosters-home.yaml`](skins/fosters-home.yaml) |
| **The Grim Adventures of Billy & Mandy** | Grim, Billy and Mandy — the weirdest trio this side of Endsville. | [`grim-adventures-of-billy-mandy.yaml`](skins/grim-adventures-of-billy-mandy.yaml) |
| **Samurai Jack** | A samurai trapped in a future ruled by the demon Aku. | [`samurai-jack.yaml`](skins/samurai-jack.yaml) |
| **Cow and Chicken** | The adventures of a cow and her chicken brother. | [`cow-and-chicken.yaml`](skins/cow-and-chicken.yaml) |
| **I Am Weasel** | I.M. Weasel, the brilliant one — and I.R. Baboon, his rival. | [`i-am-weasel.yaml`](skins/i-am-weasel.yaml) |
| **2 Stupid Dogs** | Little Dog and Big Dog — the two dumbest, happiest dogs around. | [`2-stupid-dogs.yaml`](skins/2-stupid-dogs.yaml) |
| **Whatever Happened to Robot Jones?** | A robot kid navigating middle school in a retro-future. | [`robot-jones.yaml`](skins/robot-jones.yaml) |
| **Mike, Lu & Og** | A city girl, a genius and a native boy on a tropical island. | [`mike-lu-og.yaml`](skins/mike-lu-og.yaml) |
| **Sheep in the Big City** | An escaped military sheep living in the big city. | [`sheep-in-the-big-city.yaml`](skins/sheep-in-the-big-city.yaml) |
| **The Cramp Twins** | Identical twin brothers with opposite personalities. | [`the-cramp-twins.yaml`](skins/the-cramp-twins.yaml) |
| **Camp Lazlo** | Lazlo the bean scout monkey and the campers of Camp Kidney. | [`camp-lazlo.yaml`](skins/camp-lazlo.yaml) |
| **My Gym Partner's a Monkey** | A boy transferred to a school for animals. | [`my-gym-partner-is-a-monkey.yaml`](skins/my-gym-partner-is-a-monkey.yaml) |
| **Squirrel Boy** | A boy and his loud, squirrel best friend. | [`squirrel-boy.yaml`](skins/squirrel-boy.yaml) |
| **Hi Hi Puffy AmiYumi** | The real-life rock duo as cartoon adventures. | [`hi-hi-puffy-amiyumi.yaml`](skins/hi-hi-puffy-amiyumi.yaml) |
| **The Life and Times of Juniper Lee** | An 11-year-old secretly protecting the world from monsters. | [`juniper-lee.yaml`](skins/juniper-lee.yaml) |
| **Class of 3000** | Andre 3000 teaches music at a school in Atlanta. | [`class-of-3000.yaml`](skins/class-of-3000.yaml) |
| **Mucha Lucha!** | Masked luchadores wrestling for honor at the International School of Lucha. | [`mucha-lucha.yaml`](skins/mucha-lucha.yaml) |
| **The Problem Solverz** | Neon-soaked adventures with Alfe, Robo and Horace. | [`the-problem-solverz.yaml`](skins/the-problem-solverz.yaml) |
| **Out of Jimmy's Head** | Live-action and cartoon — whatever Jimmy imagines, gets out. | [`out-of-jimmys-head.yaml`](skins/out-of-jimmys-head.yaml) |
| **Chowder** | An apprentice chef with a big appetite and a bigger imagination. | [`chowder.yaml`](skins/chowder.yaml) |
| **The Marvelous Misadventures of Flapjack** | A boy and a pirate captain searching for Candied Island. | [`flapjack.yaml`](skins/flapjack.yaml) |
| **Total Drama** | Reality TV satire — 22 campers, one island, zero mercy. | [`total-drama.yaml`](skins/total-drama.yaml) |
| **Total DramaRama** | The Total Drama cast as chaotic toddlers. | [`total-dramarama.yaml`](skins/total-dramarama.yaml) |
| **6teen** | Six teens working and hanging out at the Galleria mall. | [`6teen.yaml`](skins/6teen.yaml) |
| **Stoked** | Six teens working a summer at a surf resort. | [`stoked.yaml`](skins/stoked.yaml) |
| **Robotboy** | A top-secret battle robot living with a normal family. | [`robotboy.yaml`](skins/robotboy.yaml) |
| **Megas XLR** | A giant robot from the future, a slacker driver and a mechanic. | [`megas-xlr.yaml`](skins/megas-xlr.yaml) |
| **Xiaolin Showdown** | Monk warriors collecting Shen Gong Wu artifacts. | [`xiaolin-showdown.yaml`](skins/xiaolin-showdown.yaml) |
| **The Secret Saturdays** | A cryptozoologist family hunting legendary creatures. | [`secret-saturdays.yaml`](skins/secret-saturdays.yaml) |
| **Sym-Bionic Titan** | Three alien teens pilot a giant mech to defend Earth. | [`sym-bionic-titan.yaml`](skins/sym-bionic-titan.yaml) |
| **Hero: 108** | Hidden Valley's secret animal army faces the HighRollers. | [`hero-108.yaml`](skins/hero-108.yaml) |
| **Chop Socky Chooks** | Three kung-fu chickens defending their fish-and-chip shop. | [`chop-socky-chooks.yaml`](skins/chop-socky-chooks.yaml) |
| **Skatoony** | Skateboarding quiz show — answer or wipe out! | [`skatoony.yaml`](skins/skatoony.yaml) |
| **Hot Wheels Battle Force 5** | Racing cars with weapons, defending Earth from the Sark. | [`hot-wheels-battle-force-5.yaml`](skins/hot-wheels-battle-force-5.yaml) |
| **Monster Beach** | Surfing monsters living at the graveyard shore. | [`monster-beach.yaml`](skins/monster-beach.yaml) |
| **Duck Dodgers** | Daffy Duck as the 24th-and-a-half-century space hero. | [`ducks-dodgers.yaml`](skins/ducks-dodgers.yaml) |
| **Loonatics Unleashed** | Futuristic descendants of the Looney Tunes saving Metropolis. | [`loonatics-unleashed.yaml`](skins/loonatics-unleashed.yaml) |
| **Baby Looney Tunes** | The classic characters as toddlers in daycare. | [`baby-looney-tunes.yaml`](skins/baby-looney-tunes.yaml) |
| **Krypto the Superdog** | Superman's dog protecting Metropolis as a family pet. | [`krypto-superdog.yaml`](skins/krypto-superdog.yaml) |

### Modern Cartoon Network

| Skin | Description | File |
|------|-------------|------|
| **Adventure Time** | Finn and Jake's mathematical quests across the Land of Ooo. | [`adventure-time.yaml`](skins/adventure-time.yaml) |
| **Regular Show** | Mordecai and Rigby's very regular, very weird park jobs. | [`regular-show.yaml`](skins/regular-show.yaml) |
| **The Amazing World of Gumball** | A blue cat and a goldfish navigating Elmore's chaos. | [`the-amazing-world-of-gumball.yaml`](skins/the-amazing-world-of-gumball.yaml) |
| **Steven Universe** | A half-gem boy learning to protect Beach City with the Crystal Gems. | [`steven-universe.yaml`](skins/steven-universe.yaml) |
| **We Bare Bears** | Grizz, Panda and Ice Bear trying to fit in with humans. | [`we-bare-bears.yaml`](skins/we-bare-bears.yaml) |
| **We Baby Bears** | The baby bears' adventures through magical portals. | [`we-baby-bears.yaml`](skins/we-baby-bears.yaml) |
| **Uncle Grandpa** | Everyone's magical uncle and grandpa who only exists to help. | [`uncle-grandpa.yaml`](skins/uncle-grandpa.yaml) |
| **Clarence** | A relentlessly sunny kid and his friends in Aberdale. | [`clarence.yaml`](skins/clarence.yaml) |
| **Craig of the Creek** | Craig and his crew exploring the kid-ruled creek. | [`craig-of-the-creek.yaml`](skins/craig-of-the-creek.yaml) |
| **OK K.O.! Let's Be Heroes** | K.O. trains to be a hero at Lakewood Plaza Turbo. | [`ok-ko.yaml`](skins/ok-ko.yaml) |
| **Infinity Train** | Passengers ride an endless train solving their personal issues. | [`infinity-train.yaml`](skins/infinity-train.yaml) |
| **Apple & Onion** | Two food friends chasing their dreams in the big city. | [`apple-onion.yaml`](skins/apple-onion.yaml) |
| **Victor and Valentino** | Two brothers exploring a Mexican folklore town. | [`victor-valentino.yaml`](skins/victor-valentino.yaml) |
| **Mao Mao: Heroes of Pure Heart** | A hot-tempered sheriff cat defending Pure Heart Valley. | [`mao-mao.yaml`](skins/mao-mao.yaml) |
| **Summer Camp Island** | A magical summer camp where nothing is quite normal. | [`summer-camp-island.yaml`](skins/summer-camp-island.yaml) |
| **Elliott from Earth** | A boy, his mom and a dinosaur stranded on Earth. | [`elliott-from-earth.yaml`](skins/elliott-from-earth.yaml) |
| **Mighty Magiswords** | Prohyas and Vambre collect magical swords for quests. | [`mighty-magiswords.yaml`](skins/mighty-magiswords.yaml) |
| **The High Fructose Adventures of Annoying Orange** | The obnoxious fruit that never stops talking. | [`annoying-orange.yaml`](skins/annoying-orange.yaml) |
| **Teen Titans Go!** | The Titans' silly, snack-fueled side adventures. | [`teen-titans-go.yaml`](skins/teen-titans-go.yaml) |
| **Jade Armor** | A teen girl discovers a legendary jade armor. | [`jade-armor.yaml`](skins/jade-armor.yaml) |
| **Unikitty** | The LEGO princess of rage and happiness in Unikittyland. | [`unikitty.yaml`](skins/unikitty.yaml) |
| **Mixels** | Mix and match creatures from the Nixel-infested Mixel world. | [`mixels.yaml`](skins/mixels.yaml) |
| **ThunderCats Roar** | The goofy 2019 reboot of the classic cat heroes. | [`thundercats-roar.yaml`](skins/thundercats-roar.yaml) |
| **DreamWorks Dragons** | Hiccup and Toothless' adventures from the Dragon franchise. | [`dreamworks-dragons.yaml`](skins/dreamworks-dragons.yaml) |

### DC Super Heroes

| Skin | Description | File |
|------|-------------|------|
| **Teen Titans** | The classic Titans — Robin, Starfire, Raven, Cyborg and Beast Boy. | [`teen-titans.yaml`](skins/teen-titans.yaml) |
| **Justice League** | Earth's mightiest heroes united as one team. | [`justice-league.yaml`](skins/justice-league.yaml) |
| **Justice League Unlimited** | The expanded league with dozens of heroes in action. | [`justice-league-unlimited.yaml`](skins/justice-league-unlimited.yaml) |
| **Batman: The Animated Series** | The Dark Knight of Gotham in the definitive animated take. | [`batman-tas.yaml`](skins/batman-tas.yaml) |
| **Batman Beyond** | A teenager inherits the Batsuit in Neo-Gotham. | [`batman-beyond.yaml`](skins/batman-beyond.yaml) |
| **Static Shock** | Virgil Hawkins — the electric superhero of Dakota. | [`static-shock.yaml`](skins/static-shock.yaml) |
| **The Zeta Project** | A prototype spy robot trying to prove he's not a weapon. | [`zeta-project.yaml`](skins/zeta-project.yaml) |
| **Young Justice** | The teen sidekicks operating as a covert team. | [`young-justice.yaml`](skins/young-justice.yaml) |
| **Green Lantern: The Animated Series** | Hal Jordan and Kilowog patrolling the universe. | [`green-lantern-tas.yaml`](skins/green-lantern-tas.yaml) |
| **Beware the Batman** | The 2013 Batman series focused on Detective Gordon and Katana. | [`beware-the-batman.yaml`](skins/beware-the-batman.yaml) |
| **Justice League Action** | Fast-paced, fun-sized league adventures. | [`justice-league-action.yaml`](skins/justice-league-action.yaml) |
| **DC Super Hero Girls** | Super-powered teens balancing heroics and high school. | [`dc-super-hero-girls.yaml`](skins/dc-super-hero-girls.yaml) |
| **Batman: The Brave and the Bold** | Batman teaming up with heroes across the DC universe. | [`batman-brave-bold.yaml`](skins/batman-brave-bold.yaml) |

### Star Wars & LEGO

| Skin | Description | File |
|------|-------------|------|
| **Star Wars: The Clone Wars** | Anakin, Obi-Wan and the clones in the Clone Wars era. | [`star-wars-clone-wars.yaml`](skins/star-wars-clone-wars.yaml) |
| **Ninjago: Masters of Spinjitzu** | Elemental ninja protect Ninjago from the forces of darkness. | [`ninjago.yaml`](skins/ninjago.yaml) |
| **LEGO Monkie Kid** | MK wields the Monkey King's staff against demons. | [`lego-monkie-kid.yaml`](skins/lego-monkie-kid.yaml) |
| **LEGO City Adventures** | Everyday heroes of LEGO City — cops, firefighters and more. | [`lego-city-adventures.yaml`](skins/lego-city-adventures.yaml) |
| **ThunderCats (2011)** | Lion-O and the ThunderCats rebuild after Thundera's fall. | [`thundercats-2011.yaml`](skins/thundercats-2011.yaml) |

### Toonami & Action

| Skin | Description | File |
|------|-------------|------|
| **Toonami** | The legendary action block — TOM's late-night anime lineup. | [`toonami.yaml`](skins/toonami.yaml) |
| **Dragon Ball Z** | Goku and the Z-Fighters defending Earth from planet-level threats. | [`dragon-ball-z.yaml`](skins/dragon-ball-z.yaml) |
| **Dragon Ball GT** | Goku shrunk to a kid, searching the Black Star Dragon Balls. | [`dragon-ball-gt.yaml`](skins/dragon-ball-gt.yaml) |
| **Dragon Ball Super** | Gods of Destruction, tournaments and Ultra Instinct. | [`dragon-ball-super.yaml`](skins/dragon-ball-super.yaml) |
| **Naruto** | A loud ninja with a dream of becoming Hokage. | [`naruto.yaml`](skins/naruto.yaml) |
| **Naruto Shippuden** | Naruto's older, darker journey to bring Sasuke home. | [`naruto-shippuden.yaml`](skins/naruto-shippuden.yaml) |
| **One Piece** | Monkey D. Luffy's quest for the One Piece and the Pirate King title. | [`one-piece.yaml`](skins/one-piece.yaml) |
| **Bleach** | Ichigo Kurosaki, the substitute Soul Reaper. | [`bleach.yaml`](skins/bleach.yaml) |
| **Cowboy Bebop** | Bounty hunters in space, jazz in the background. | [`cowboy-bebop.yaml`](skins/cowboy-bebop.yaml) |
| **Samurai Champloo** | Hip-hop samurai road trip across Edo Japan. | [`samurai-champloo.yaml`](skins/samurai-champloo.yaml) |
| **Eureka Seven** | Renton pilots the Nirvash and rides the trapar waves. | [`eureka-seven.yaml`](skins/eureka-seven.yaml) |
| **Inuyasha** | A half-demon and a schoolgirl hunting Shikon shards. | [`inuyasha.yaml`](skins/inuyasha.yaml) |
| **Fullmetal Alchemist** | Two brothers and the law of equivalent exchange. | [`fullmetal-alchemist.yaml`](skins/fullmetal-alchemist.yaml) |
| **Yu Yu Hakusho** | Spirit detective Yusuke fighting the demon world. | [`yu-yu-hakusho.yaml`](skins/yu-yu-hakusho.yaml) |
| **Hunter x Hunter** | Gon and Killua take the Hunter Exam and master Nen. | [`hunter-x-hunter.yaml`](skins/hunter-x-hunter.yaml) |
| **Attack on Titan** | Humanity fights for survival against the Titans. | [`attack-on-titan.yaml`](skins/attack-on-titan.yaml) |
| **My Hero Academia** | Deku trains to become the greatest hero at UA. | [`my-hero-academia.yaml`](skins/my-hero-academia.yaml) |
| **JoJo's Bizarre Adventure** | Generations of Joestars and their Stands. | [`jojo-bizarre-adventure.yaml`](skins/jojo-bizarre-adventure.yaml) |
| **Mob Psycho 100** | A powerful psychic trying to live an ordinary life. | [`mob-psycho-100.yaml`](skins/mob-psycho-100.yaml) |
| **Demon Slayer** | Tanjiro's quest to cure his sister and slay demons. | [`demon-slayer.yaml`](skins/demon-slayer.yaml) |
| **Sword Art Online** | Players trapped in a deadly VRMMO must clear the game. | [`sword-art-online.yaml`](skins/sword-art-online.yaml) |
| **One Punch Man** | Saitama ends every fight with one punch. | [`one-punch-man.yaml`](skins/one-punch-man.yaml) |
| **Dr. Stone** | Senku rebuilds civilization from stone with science. | [`dr-stone.yaml`](skins/dr-stone.yaml) |
| **Fire Force** | Special fire brigades fighting Infernals with flames. | [`fire-force.yaml`](skins/fire-force.yaml) |
| **Mobile Suit Gundam Wing** | Five Gundam pilots and their fight for the colonies. | [`gundam-wing.yaml`](skins/gundam-wing.yaml) |
| **Mobile Suit Gundam 00** | Celestial Being intervenes to end war with Gundams. | [`gundam-00.yaml`](skins/gundam-00.yaml) |
| **Space Dandy** | The dandy guy in space, hunting rare aliens. | [`space-dandy.yaml`](skins/space-dandy.yaml) |
| **FLCL** | The surreal coming-of-age story with guitars and robots. | [`flcl.yaml`](skins/flcl.yaml) |
| **The Big O** | Roger Smith and the giant robot Big O in Paradigm City. | [`big-o.yaml`](skins/big-o.yaml) |
| **Mobile Fighter G Gundam** | The Gundam Fight tournament decides Earth's fate. | [`g-gundam.yaml`](skins/g-gundam.yaml) |
| **Tenchi Muyo** | An ordinary guy with extraordinary space friends. | [`tenchi-muyo.yaml`](skins/tenchi-muyo.yaml) |
| **Sailor Moon** | Usagi and the Sailor Guardians fight evil by moonlight. | [`sailor-moon.yaml`](skins/sailor-moon.yaml) |
| **Zoids** | Mecha beasts battling across the planet Zi. | [`zoids.yaml`](skins/zoids.yaml) |
| **Outlaw Star** | Gene Starwind and the search for the Galactic Leyline. | [`outlaw-star.yaml`](skins/outlaw-star.yaml) |
| **Rurouni Kenshin** | A wandering swordsman protecting the Meiji era. | [`rurouni-kenshin.yaml`](skins/rurouni-kenshin.yaml) |
| **Deadman Wonderland** | Ganta fights for survival in a deadly prison. | [`deadman-wonderland.yaml`](skins/deadman-wonderland.yaml) |
| **Trigun** | Vash the Stampede — the pacifist gunslinger with a $$60 billion bounty. | [`trigun.yaml`](skins/trigun.yaml) |
| **Bakugan** | Battle brawlers with cards that spring into creatures. | [`bakugan.yaml`](skins/bakugan.yaml) |
| **Beyblade** | Spinning tops battle it out in the beystadium. | [`beyblade.yaml`](skins/beyblade.yaml) |
| **Beyblade Burst** | The Burst era — beys that burst apart at high speed. | [`beyblade-burst.yaml`](skins/beyblade-burst.yaml) |

### Adult Swim

| Skin | Description | File |
|------|-------------|------|
| **Rick and Morty** | A genius mad scientist and his grandson across dimensions. | [`rick-and-morty.yaml`](skins/rick-and-morty.yaml) |
| **Aqua Teen Hunger Force** | Master Shake, Frylock and Meatwad's bizarre suburban life. | [`aqua-teen-hunger-force.yaml`](skins/aqua-teen-hunger-force.yaml) |
| **Robot Chicken** | Stop-motion sketch comedy with pop-culture mayhem. | [`robot-chicken.yaml`](skins/robot-chicken.yaml) |
| **Space Ghost Coast to Coast** | A retired superhero hosts a talk show. | [`space-ghost-coast-to-coast.yaml`](skins/space-ghost-coast-to-coast.yaml) |
| **Harvey Birdman, Attorney at Law** | A superhero lawyer defending cartoon characters. | [`harvey-birdman.yaml`](skins/harvey-birdman.yaml) |
| **Sealab 2021** | A dysfunctional underwater research station. | [`sealab-2021.yaml`](skins/sealab-2021.yaml) |
| **The Venture Bros.** | The Venture family — failed scientists and bodyguards. | [`venture-bros.yaml`](skins/venture-bros.yaml) |
| **Metalocalypse** | The world's greatest death metal band, Dethklok. | [`metalocalypse.yaml`](skins/metalocalypse.yaml) |
| **Squidbillies** | Squid-mountain-dwellers causing trouble in the backwoods. | [`squidbillies.yaml`](skins/squidbillies.yaml) |

### Acquired & International

| Skin | Description | File |
|------|-------------|------|
| **Tom and Jerry** | The eternal cat-and-mouse chase that needs no intro. | [`tom-and-jerry.yaml`](skins/tom-and-jerry.yaml) |
| **Scooby-Doo** | Mystery Inc. and the Mystery Machine solving spooky cases. | [`scooby-doo.yaml`](skins/scooby-doo.yaml) |
| **What's New, Scooby-Doo?** | The 2000s Mystery Inc. — same gang, new mysteries. | [`whats-new-scooby-doo.yaml`](skins/whats-new-scooby-doo.yaml) |
| **Scooby-Doo! Mystery Incorporated** | The darker serialized Mystery Inc. mystery. | [`scooby-doo-mystery-incorporated.yaml`](skins/scooby-doo-mystery-incorporated.yaml) |
| **Johnny Test** | A boy and his genius sisters' experiments. | [`johnny-test.yaml`](skins/johnny-test.yaml) |
| **The Garfield Show** | The lasagna-loving cat and his friends. | [`garfield-show.yaml`](skins/garfield-show.yaml) |
| **Oggy and the Cockroaches** | A cat's quiet life ruined by three cockroaches. | [`oggy-cockroaches.yaml`](skins/oggy-cockroaches.yaml) |
| **Zig & Sharko** | A hyena's endless attempts to catch a mermaid. | [`zig-sharko.yaml`](skins/zig-sharko.yaml) |
| **Grizzy and the Lemmings** | A bear vs. the lemmings in a national park cabin. | [`grizzy-lemmings.yaml`](skins/grizzy-lemmings.yaml) |
| **Mr. Bean: The Animated Series** | The beloved bumbling everyman, animated. | [`mr-bean-animated.yaml`](skins/mr-bean-animated.yaml) |
| **Taffy** | A crafty cat and a dog in a mansion full of schemes. | [`taffy.yaml`](skins/taffy.yaml) |
| **Angelo Rules** | A boy using elaborate plans to get what he wants. | [`angelo-rules.yaml`](skins/angelo-rules.yaml) |
| **Transformers: Animated** | The Autobots as a repair crew in Detroit. | [`transformers-animated.yaml`](skins/transformers-animated.yaml) |
| **Code Lyoko** | Virtual warriors entering Lyoko to fight XANA. | [`code-lyoko.yaml`](skins/code-lyoko.yaml) |
| **Mega Man: Fully Charged** | The blue bomber reborn for a new generation. | [`mega-man-fully-charged.yaml`](skins/mega-man-fully-charged.yaml) |

### Cartoon Network India

| Skin | Description | File |
|------|-------------|------|
| **Roll No. 21** | Krishna, the mischievous kid who gets into magical trouble. | [`roll-no-21.yaml`](skins/roll-no-21.yaml) |
| **Pakdam Pakdai** | Cat vs. mouse in a wacky, fast-paced chase. | [`pakdam-pakdai.yaml`](skins/pakdam-pakdai.yaml) |
| **Gattu Battu** | A boy and his faithful dog on everyday adventures. | [`gattu-battu.yaml`](skins/gattu-battu.yaml) |
| **Rohan & Anisha** | A boy and his alien friend's city adventures. | [`rohan-anisha.yaml`](skins/rohan-anisha.yaml) |
| **Kumbh Karan** | The sleepy giant from the legends, now a lovable kid. | [`kumbh-karan.yaml`](skins/kumbh-karan.yaml) |
| **Chumbak** | A magnet-powered kid attracting adventure. | [`chumbak.yaml`](skins/chumbak.yaml) |
| **Viramputin** | A cartoonist's characters come to life in a wild town. | [`viramputin.yaml`](skins/viramputin.yaml) |
| **Supa Strikas** | The world's best street football team. | [`supa-strikas.yaml`](skins/supa-strikas.yaml) |
| **Lamput** | A blob of orange goo outsmarting two lab scientists. | [`lamput.yaml`](skins/lamput.yaml) |

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
