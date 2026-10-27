from lib import Page

DECL1 = ("❌ No thanks — I'll try to build my own predictable repeatable ads process alone",
         "(even if it takes months and costs thousands in figuring it all out)")

def offer_price(P, regular, main, unit, note=''):
    n = f'<small>{note}</small>' if note else ''
    P.raw(f'<p class="price">Regular Price: <s>{regular}</s><br>Yours today: <b class="big">{main}</b> {unit}{n}</p>')

# ---------------------------------------------------------------- OTO / DS 1
def oto1():
    P=Page()
    P.warn("⚠️ IMPORTANT — Your order is not complete. Do not close this page.")
    P.p("*You have one chance to see what's below. It disappears the moment you click away.*")
    P.kicker("Booked on autopilot · Before you go")
    P.h1("Congratulations! You Just Did What Most Painters Never Do.")
    P.p("They read the page. They know it would help them. But then they doubt themselves and close the tab.",
        "That's not you. You stopped waiting and made a move.")
    P.h2("The Playbook Gets Homeowners Raising Their Hand. But Something Has To Catch Them The Moment They Do.")
    P.p("**From the desk of Lanty**\nFounder, Home Pro Jobs",
        "I started as a painting contractor myself.",
        "Not a marketer who stumbled into the trades. A painter who built crews, ran estimates, chased leads, and figured out the hard way what actually works in this business.")
    P.ul(["**$4M+** — gross revenue, 5 years","**$1M** — on track this year","**25%** — profit margins","**$15** — cost per lead"])
    P.p("Over the last five years, our painting operation generated over $4 million in gross revenue. This year we're on track for $1 million — with 25% profit margins.",
        "We got there because we stopped doing what everyone else was doing.")
    P.ul(["Referral grinding","Post-and-pray","Cold calling homeowner lists"])
    P.p("We built a system that brought $15 leads into our own inbox, converted them to appointments at 60%, and closed 40% of those estimates to signed jobs.",
        "That system is what the Super Paint Close Playbook teaches.",
        "What I'm about to show you on this page is how we made sure none of those leads slipped through the cracks once they came in.",
        "Because the second we got our response time under five minutes — the calendar never had a gap again.",
        "That's the one thing I'm going to show you how to install today.")
    P.h2("This Is For You")
    P.p("This page is for you if:")
    P.chk(["You are a painting contractor running residential jobs and you want a consistent, predictable flow of booked estimates coming into your calendar — without spending your evenings chasing leads.",
           "You have posted on Facebook or neighborhood groups before, got some interest, and then watched the leads go cold before you could get back to them. You know the problem wasn't the post. It was the gap between the lead coming in and someone picking up the phone.",
           "You are busy enough on the tools that you cannot also be the person monitoring the inbox, texting new leads within minutes, and handling all the appointment booking on top of running a crew.",
           "You want the business to work harder than you do — leads come in, someone qualifies them, appointments land in your calendar, and you show up to the estimate while the machine keeps running in the background.",
           "You understand that one closed job at $3,500 pays for months of this — and that math doesn't feel like a stretch to you. It feels obvious."])
    P.h2("This Is Not For You")
    P.p("This page is not for you if:")
    P.no(["You are not yet actively running a residential painting business and quoting jobs.",
          "You want to stay fully in control of every lead conversation yourself and prefer to handle your own follow-up your own way.",
          "You are expecting leads to turn into jobs without showing up to the estimate and closing the work.",
          "You want to think about it for a few weeks — because the window on this offer does not stay open."])
    P.h2("Here Is What Is About To Happen")
    P.ol(["You share the post.","A homeowner in your area sees it.","They're interested.","They fill out the form."])
    P.p("**And then — they wait.**",
        "You're wrapping a job.\nYour phone is in the truck.\nYou don't see the notification for two hours.",
        "By the time you text back — they already booked with the painter who called them in four minutes.",
        "That job was yours. You did everything right. You ran the post, you got the lead. And you still lost it.",
        "Not because your price was wrong.\nNot because your work wasn't good enough.",
        "Because there was a gap.",
        "A gap between the moment the lead came in and the moment someone picked up the phone.",
        "That gap is silent. You never see it happen.",
        "The lead just goes cold and you move on, not knowing what you lost.")
    P.h2("Here Is What The Numbers Say About Painting Leads.",eyebrow="The proof")
    P.box("**RESPONDS IN UNDER 5 MINUTES: 80%+**\nA painter who responds to a fresh lead in under five minutes books the estimate more than 80% of the time.")
    P.box("**WAITS 2 HOURS: <20%**\nThat same painter — waiting two hours on the same lead, same homeowner, same job — books it less than 20% of the time.")
    P.p("Same post.\nSame price.\nSame quality of work.",
        "The only thing that changed is the five-minute window.",
        "That's the whole game.",
        "And that's the only thing left between you and a full calendar.")
    P.h2("So Here Is Where You Are Right Now")
    P.p("**You have:** The Playbook. That's the engine.",
        "**But:** An engine without a driver leaves jobs on the table.",
        "Right now — when a lead comes in at 6:45pm on a Tuesday while you're finishing a job — who picks up that call?",
        "What you're about to see gives you a better answer than “me, whenever I can get to it.”",
        "Two options. Both build directly on the Playbook. Both close the gap.",
        "**The first option (below)** hands you the tools and you run the inbox yourself.",
        "**The second option (below, marked BEST OPTION)** does it completely for you.",
        "Look at both. One of them is exactly where you are right now.")
    # --- Option 1: DS
    P.raw('<hr>')
    P.h2("We Get You Leads",eyebrow="Option 1 — You run the inbox")
    offer_price(P,"$497/mo","$247","/mo")
    P.p("We build and turn on one Facebook Messenger ad for you.",
        "When a homeowner clicks it, they land in your Facebook inbox. You get the notification. You reply with the copy-paste script we give you. You book the appointment yourself.")
    P.p("**Here is what's included:**")
    P.chk(["Facebook Messenger ad built and activated within 48 hours","Ad targeting set up for your service area","Inbox reply script — copy-paste ready","3-message follow-up sequence for leads that go quiet"])
    P.no(["No team following up within 5 minutes","No appointments booked into your calendar","No weekly performance reporting","No Profits Vault — the 10-module business training","No 1-Hour Coaching Call with Lanty"])
    P.p("**What you handle:** The conversation, the follow-up, and the booking.",
        "For only $200 more, every single one of those is covered for you — see the full option below.",
        "If volume grows faster than you can keep up with, you can upgrade to We Get You Booked at any time for just the $250 difference. Nothing is lost.")
    P.btn("Yes — Confirm We Get You Leads →","trg-ds-yes")
    # --- Option 2: OTO
    P.raw('<hr>')
    P.h2("We Get You Booked",eyebrow="★ BEST OPTION — Done for you")
    P.raw('<p class="price">Regular Price: <s>$697/mo</s><br>Yours today: <b class="big nobreak">Just add $200</b> <span class="nobreak">more per month</span><small>($497/mo total)</small></p>')
    P.p("We run the ad. We follow up with every lead within five minutes. We book confirmed estimates straight into your calendar.",
        "Your job is to show up to the estimate. That's it.",
        "When a lead hits at 6:45pm — our team picks it up. They text, they call, they follow up until the appointment is set. It appears in your Google Calendar. You didn't do a single thing between the lead coming in and the estimate on your books.")
    P.p("**Everything included:**")
    P.chk(["Facebook ad written, built, and live within 48 hours","Every lead followed up by our team within 5 minutes — text and phone","Confirmed estimates booked straight into your Google Calendar","Weekly report: leads in, appointments set, estimates booked",
           "**INCLUDED:** The Profits Vault — 10 modules on the full business side of painting. Job costing, closing, crew structure, cash flow, reading your numbers. Yours on Day 1, kept permanently even if you leave.",
           "**FREE:** 1-Hour Private Coaching Call with Lanty — book it in your first 30 days. Bring your numbers, your market, your close rate. Yours free today."])
    P.h3("The math.")
    P.p("Five confirmed estimates a month. Average job $3,500. One closed job pays the retainer. The other four are margin you didn't have before.",
        "That's $200 more than the option above — and zero inbox management, zero follow-up, zero booking on your end. The team handles all of it.")
    P.btn("Yes — Confirm We Get You Booked →","trg-oto-yes")
    P.decline(*DECL1)
    P.h2("Once We Get You Booked Is Running — Here's What Happens",eyebrow="Picture it")
    P.ul(["Your calendar gets filled with confirmed estimates, automatically — homeowners who said yes before you even picked up the phone.",
          "Every lead that comes in gets a callback within five minutes, whether you're on a ladder, driving to a job, or putting the kids to bed.",
          "No more “I'll follow up tomorrow” leading into never. The lead gets worked the moment it comes in.",
          "That slow week you've been dreading — the one where the phone goes quiet and you start wondering where the next job is coming from — stops being a thing you have to manage.",
          "You show up to the estimate. You do the work you're actually good at. The machine handles everything before that point."])
    P.h2("Still On The Fence About The Full Option?",eyebrow="For just $200 more")
    P.p("Here is what $200 more actually buys you.",
        "**Option 1 — We Get You Leads · $247/mo**\nTurns on the ad and delivers leads to your inbox. You follow up. You book. You manage the conversation.",
        "**Option 2 — We Get You Booked · $497/mo**\nDoes all of that for you.")
    P.ul(["For $200 more, you never touch the inbox.","For $200 more, you never chase a lead that went quiet.","For $200 more, every confirmed estimate lands in your Google Calendar while you are already on a job."])
    P.p("Here is what it would cost to build that follow-up and booking system yourself:")
    P.ul(["A VA to monitor the inbox and follow up within 5 minutes — **~$800/mo**","A setter to qualify leads and book appointments — **~$600/mo**","Your own time managing the back-and-forth every evening — **+ your hourly rate**"])
    P.box("**$1,400+** a month to piece it together.\nOr **$497** to have our team run it.",red=True)
    P.p("The math does not leave a lot of room for debate.",
        "If you went with We Get You Leads and want to upgrade, you can do it at any time for just the $250 difference. The door stays open.",
        "But if you are going to make the move — make it now, while you are already here and the decision is in front of you.")
    P.h2("Your Two Options Again")
    P.p("**Option 1 — We Get You Leads:** ~~$497/mo~~ **$247/mo**. You run the inbox.")
    P.btn("Yes — Confirm We Get You Leads →","trg-ds-yes")
    P.p("**Option 2 — We Get You Booked (BEST OPTION):** ~~$697/mo~~ **Just add $200** more per month ($497/mo total). We do it all.")
    P.btn("Yes — Confirm We Get You Booked →","trg-oto-yes")
    P.h2("Right Now, Two Things Are True.")
    P.ol(["The Playbook is already getting homeowners to raise their hand.","And the painter who responds fastest wins the job. Every time."])
    P.p("That's true whether you pick the first option or the second.",
        "The only question is: when that hand goes up at 6:45 on a Tuesday night — are you the one working the inbox, or is someone else handling it while you're finishing the job?",
        "One of those costs you time you don't have.",
        "The other costs you $497 and fills your calendar while you sleep.",
        "Pick the one that makes sense for where you are right now. Then let's get to work.")
    P.decline(*DECL1)
    P.fine(support=False)
    return P

# ---------------------------------------------------------------- OTO / DS 2
def oto2():
    P=Page()
    P.warn("⚠️ IMPORTANT — Your order is almost complete. We're adding a bonus gift customization for your business.")
    P.p("While that's being done, do not close this page or hit the back button. *You have one chance to see what's below. It disappears the moment you click away.*")
    P.kicker("Your page is almost ready · Before you go")
    P.h1("You Just Made A Move Most Painters Never Make.")
    P.p("Leads are either already on their way in — or about to be.",
        "There's one thing left to set up before any of that matters.")
    P.h2("Every Post You Share Is Sending People Somewhere. Right Now, That Somewhere Is A Dead End.",eyebrow="Think about your last post")
    P.p("Think about the last post you shared.",
        "*(Not the ad we're going to do for you — a post you shared yourself.)*")
    P.ul(["A job photo.","A before-and-after.","A neighborhood shoutout."])
    P.ol(["Someone in your area saw it.","They were interested.","They clicked your name."])
    P.p("**Next: Where did they go?**",
        "Your Facebook profile. A phone number with nothing behind it. Or just — nothing.",
        "They looked around.\nNo form.\nNo page.\nNo clear next step.",
        "So they did what everyone does when they don't know what to do next.",
        "They left.",
        "That click was a real homeowner.",
        "Ready to book. And they walked away because there was nowhere for them to go.",
        "That is happening on every post you share right now. Every platform. Every time someone clicks.",
        "Until every link you share points to one page that catches them — those clicks are going straight into a hole you never see.")
    P.h2("This Is For You")
    P.p("This page is for you if:")
    P.chk(["You are already posting job photos, before-and-afters, or neighborhood content — and you know people are seeing it — but you have no single place to send them when they want to take the next step.",
           "You want one link you can drop into every post on every platform so that every click lands somewhere that captures the lead automatically, without you having to be there.",
           "You want to stay visible to homeowners who are not ready to book today but will be in 30 or 60 days — and you want your posts to keep showing up so you are the first name they think of when that day comes."])
    P.h2("This Is Not For You")
    P.p("This page is not for you if:")
    P.no(["You are not currently posting anything on Facebook, Instagram, Nextdoor, or neighborhood groups — and have no plans to start.",
          "You already have a landing page live with a working lead capture form and SMS trigger set up.",
          "You are happy writing your own social content every day from scratch."])
    P.h2("Your Posts Are Doing Their Job. Trust Does Not Pay The Bills. Leads Do.",eyebrow="The real problem")
    P.p("They are getting people curious. Building trust. Making homeowners in your neighborhood recognize your name.",
        "But right now there is a gap between someone trusting you enough to click and you actually getting their name and number.",
        "That gap is a landing page.",
        "One page. One form. One link you drop into every post you share — Facebook, Instagram, Nextdoor, neighborhood groups, anywhere.")
    P.ol(["A homeowner sees the job photo","They click the link","They fill out the form","An SMS fires to your phone before they have closed the tab"])
    P.p("That is the whole fix.",
        "Without it — every post you run builds awareness and converts nothing. You are doing all the right things and watching the results disappear through a hole you did not know was there.")
    P.h2("Both Options Build That Page For You")
    P.p("Live within 48 hours. One link you drop into any post on any platform. Every click now has a place to land that turns it into a lead.",
        "The difference between the two options is what happens after the page goes live.",
        "Because here is what most painters figure out too late.",
        "**A landing page** catches the people who are already ready to book.",
        "**But most homeowners** are not ready the first time they see you.",
        "They watch. They come back. They see another job. They see you showing up again on Wednesday. And then one day — when they are finally ready — they click.",
        "The question is whether you are still showing up when that day comes.",
        "That is what the 90 days of posts handle.",
        "One post a day. Already written for a painting contractor.",
        "You copy it, paste it across whatever platforms you are active on, add your link, done. Under two minutes. Your presence stays active. Your audience stays warm. And when someone is finally ready to click — you are still there.",
        "**The first option (below)** builds the page. What to post, how often, and whether you stay visible long enough for warm audiences to convert — that is entirely on you.",
        "**The second option (BEST OPTION, below)** hands you 90 days of posts already written.")
    P.raw('<hr>')
    P.h2("We Build Your Page",eyebrow="Option 1 — Page only")
    offer_price(P,"$197 one-time","$97","one-time")
    P.p("**We build the landing page.**",
        "One link for every platform — Facebook, Instagram, Nextdoor, neighborhood groups, anywhere you post. Headline, form, thank-you page, SMS trigger on every submission. Live within 48 hours. On your domain. Yours permanently.")
    P.p("**What's included:**")
    P.chk(["Landing page built and live within 48 hours","One link — works across every platform you post on","Lead capture form connected to your phone","Automated SMS trigger fires on every submission","Onboarding form to collect your domain and hosting access"])
    P.no(["No 90 days of copy-paste posts","No cross-platform content to keep your audience warm","No weekly post calendar organized and ready to go","No 1-Hour Coaching Call with Lanty"])
    P.p("**What you handle:** Writing your own posts, showing up consistently on every platform, and keeping your audience warm enough to click. The page catches them when they arrive. Getting them there is on you.",
        "For only $100 more, 90 days of posts are already written and handed to you — see the full option below.")
    P.btn("Yes — Confirm We Build Your Page →","trg-ds-yes")
    P.raw('<hr>')
    P.h2("We Build Your Funnel",eyebrow="★ BEST OPTION — Page + 90 days of posts")
    P.raw('<p class="price">Regular Price: <s>$397 one-time</s><br>Yours today: <b class="big nobreak">Just add $100</b> more, one-time<small>($197 total)</small></p>')
    P.p("We build the landing page and hand you 90 days of posts — already written, organized by week, ready to copy-paste across every platform you are active on.",
        "The page catches every click from every post you share.",
        "The 90 posts make sure you keep showing up on every platform until people are ready to click.",
        "Built once. One link. Works everywhere. Runs on its own.")
    P.p("**Everything included:**")
    P.chk(["Landing page built and live within 48 hours — headline, form, thank-you page, SMS trigger on every submission",
           "One link — drop it into any post on any platform, every click lands in the same place",
           "Built on your domain, under your name — yours permanently",
           "90 days of copy-paste posts — written for a painting contractor, organized by week, delivered as a Google Doc or Notion page",
           "Post types: job photo captions, before-and-afters, trust builders, seasonal offers, neighborhood-specific angles",
           "Cross-platform ready — same posts work on Facebook, Instagram, Nextdoor and neighborhood groups with your link dropped in",
           "Under two minutes each — copy the post, paste it, drop in the link, done"])
    P.p("**BONUS:** AI Agent trained in our $4M painting business — it does all the writing for you. *($500/HR — NOW FREE)*",
        "**BONUS:** 1-Hour Private Coaching Call with Lanty (stacks with any previous calls) — book it in your first 30 days.")
    P.h3("What this looks like in real life.")
    P.p("Monday morning you open the doc. You copy the post for that day. You paste it on Facebook. You drop it in the neighborhood group. You add the link. You head to the job.",
        "Three people click throughout the day. All three land on the same page. All three fill out the form. Three SMS notifications hit your phone by evening.",
        "That only happens when the page exists and the posts keep running.",
        "That's $100 more than the option above — and 90 days of content already written so you never have to stare at a blank screen wondering what to post.")
    P.btn("Yes — Confirm We Build Your Funnel →","trg-oto-yes")
    P.decline("❌ No thanks — I'll try to build my own money making funnel and automation alone","(even if it takes months and costs thousands in figuring it all out)")
    P.h2("Once Your Page Is Live — Here's What Changes",eyebrow="Picture it")
    P.ul(["Every post you share from this point forward has one destination. Clicks stop disappearing into nothing.",
          "Homeowners who are not ready today stay in your orbit — they see the posts, they see the jobs, they see you showing up — and when they are ready, the link is right there.",
          "You stop guessing what to post. The doc is organized by week. You open it, copy, paste, add the link, move on.",
          "The SMS fires the moment someone fills out the form. You know about the lead before they have even closed the tab.",
          "Your organic presence and your lead capture start working as one system instead of two separate things that never connect."])
    P.h2("Proof",eyebrow="Proof")
    P.p("A painter in a mid-sized market set the page live on a Thursday.",
        "By the following Monday he had four form submissions from posts he had already been running — posts that previously sent people nowhere.",
        "Same posts. Same audience. Same market.",
        "The only thing that changed was where the link pointed.")
    P.h2("Still Deciding Between The Two?",eyebrow="For just $100 more")
    P.p("Here is what $100 more actually buys you.",
        "**Option 1 — We Build Your Page · $97**\nBuilds the page. What to post, how often, and whether you stay visible long enough for warm audiences to convert — that is entirely on you.",
        "**Option 2 — We Build Your Funnel · $197**\nHands you 90 days of posts already written. You open the doc, copy, paste, add the link. Done. Every single day for 90 days.",
        "Here is what writing 90 days of targeted posts yourself actually costs:")
    P.ul(["A freelance social media writer — ~$15–25 per post — **$1,350–$2,250**","Your own time researching what to say and writing it — 90 evenings — **+ your hourly rate × 90**"])
    P.p("The posts in the full option are written specifically for a painting contractor. Job photo captions, before-and-afters, seasonal angles, neighborhood-specific trust builders. You would spend more on one night of outsourcing than the entire option costs today.")
    P.box("**$100 more — and 90 days of your content is already done.**",red=True)
    P.p("If you went with We Build Your Page and want to upgrade later, you can do it at any time for the difference. The door stays open.",
        "But the easiest time to make that call is right now, while you are already here.")
    P.btn("Upgrade to We Build Your Funnel →","trg-oto-yes")
    P.h2("Every Post You Have Shared Until Today Had The Same Problem.")
    P.p("It got people interested. They clicked. And then there was nowhere for them to go.")
    P.ol(["That ends right now.","One page. One link. Every post you share from this point forward has a place to send people that turns the click into a lead."])
    P.p("The only question is whether that page works alone — or whether it is backed by 90 days of posts keeping your audience warm on every platform until they are ready to use it.",
        "One option builds the destination. The other makes sure people keep showing up to it.",
        "The painter who sets both up today is the one still getting leads from posts he shared two months ago.",
        "Pick the one that fits. Let's keep moving.")
    P.decline("❌ No thanks — I'll try to build my own money making funnel and automation alone","(even if it takes months and costs thousands in figuring it all out)")
    P.fine(support=False)
    return P

# ---------------------------------------------------------------- OTO / DS 3
def oto3():
    P=Page()
    P.warn("⚠️ Hold on — your order is still being processed.")
    P.p("We're adding one final piece before everything is sent over. *Do not close this page.*")
    P.kicker("The last piece · Before you go")
    P.h1("One Problem Nobody Warned You About")
    P.p("You now have leads coming in and a page that catches every click.",
        "There is one problem nobody warned you about.",
        "Getting to the estimate is the easy part. Leaving with the job is where most painters lose money they already earned.")
    P.h2("You've Solved The Hardest Part Of This Business. Getting In Front Of Them. Now Here's What Determines Whether You Leave With A Deposit Or A “We'll Think About It.”",eyebrow="You pull up to the curb")
    P.p("The homeowner already knows who you are — they saw the post, clicked the link, filled out the form, and booked the estimate themselves.",
        "That almost never happened before.",
        "But here is what happens next that nobody talks about.",
        "**Three other painters are quoting the same job.**",
        "And the homeowner has already started deciding — before you knock.")
    P.ul(["**CLOCKED** — Whether you drove a clean truck or a beat-up one.","**NOTICED** — How you walked up to the door.","**FELT** — Something in the first handshake.","**NOW** — You're sitting across from them — and they've already formed an opinion."])
    P.p("Most painters show up hoping their work will speak for itself.",
        "The painters who close at 40% know the decision was already forming before they opened their mouth.")
    P.h2("This Is For You")
    P.p("This page is for you if:")
    P.chk(["You are now getting estimates booked — or you are about to be — and you want to make sure you close a high percentage of the jobs you actually show up to, not just the easy ones.",
           "You have lost estimates you thought you had, walked away with a “we'll think about it,” and never heard back — and you know the problem wasn't your price or your work. Something happened in the room.",
           "You want the words for the three moments that kill more estimates than anything else: “I need to think about it,” the spouse who wasn't home, and the homeowner sliding a competitor's quote across the table."])
    P.h2("This Is Not For You")
    P.p("This page is not for you if:")
    P.no(["You are not yet getting to the estimate stage — come back when the calendar is filling.",
          "You already have a close rate above 50% on residential estimates and a documented follow-up sequence for cold leads.",
          "You want to keep winging it at the table and figure it out as you go."])
    P.h2("The Homeowner Has Already Started Saying Yes Or No Before You Open Your Mouth.",eyebrow="The real problem")
    P.p("Every micro-moment from the second you pull up — how you look, how you knock, how you walk the property, what you say before the price ever comes out — is stacking toward a decision.",
        "**Stack enough micro yeses** before the number lands and the price almost doesn't matter.",
        "**Stack micro nos** and the price becomes the wall.",
        "When a homeowner has already decided they want you — decided before the quote — the price becomes a formality. When they haven't decided yet, the price becomes the objection.",
        "The game is not to defend the number. The game is to build the yes before the number ever comes out.",
        "One sentence at the right moment does it. Something like:")
    P.p("**THE PRE-FRAME**")
    P.quote("“I want to be upfront — we're not the cheapest option out there. Good work costs what it costs. But let me show you exactly what you're getting for it.”")
    P.p("Their guard drops. Because you just told them the number will be real money — and that honesty reads as confidence.",
        "Confidence reads as quality. And quality is what they were already hoping you'd be.",
        "By the time the actual price lands, they've already mentally prepared for something higher. The real number feels like a relief.",
        "That's the frame. And it works before a single objection is raised.")
    P.h2("Proof",eyebrow="Proof")
    P.p("A painter using the Competitor Pre-Frame Script reported closing two jobs in one week from estimates where multiple painters were quoting.",
        "Both homeowners told him the same thing after signing: “We already decided before you gave us the number.”",
        "Same market. Same prices. Same quality of work.",
        "The only thing that changed was what he said before the quote came out.")
    P.h2("The Tools On This Page Handle All Of It")
    P.ul(["**BEFORE** — What to do before you knock.","**WALK IN** — What to say when you walk in.","**BUILD** — How to build micro yeses all the way to the table.","**FRAME** — How to set the price frame so the number lands right.","**OBJECTIONS** — What to say in the three moments that kill the most estimates.","**FOLLOW-UP** — What to do with every lead that went cold after the first two texts."])
    P.p("Because the job that books on week nine of the follow-up sequence is just as real as the one that booked on day one.",
        "Again, you have two options below.",
        "**The first option (below)** gives you the single script that sets you up before any other painter even arrives to quote.",
        "**The second option (BEST OPTION)** gives you the whole system — from the moment you pull up to the curb to the follow-up text nine weeks after they went quiet.")
    P.raw('<hr>')
    P.h2("We Pre-Frame Your Close",eyebrow="Option 1 — One script")
    offer_price(P,"$67 one-time","$27","one-time")
    P.p("**One script.** For the moment a homeowner tells you other painters are coming out to quote.",
        "One question that shifts how they compare you. One statement that positions you as the obvious choice before anyone else walks through their door. Works on the phone, in a text, or face to face.")
    P.p("**What's included:**")
    P.chk(["Competitor Pre-Frame Script — single page, copy-paste or read verbatim"])
    P.no(["No First Impression Protocol — no guidance on how to show up, knock, or stack micro yeses","No Price Frame — no way to set expectations before the number comes out","No Estimate Close Card — no words for the three objections that kill most estimates","No 90-Day Cold Lead Follow-Up Sequence","No 1-Hour Coaching Call with Lanty"])
    P.p("**What you handle:** Everything else at the estimate — how you show up, how you set the price frame, how you handle objections at the table, and what you do with leads that went cold. The pre-frame sets you up before you arrive. The rest is still on you.",
        "For only $20 more, every one of those is handled — see the full option below.")
    P.btn("Yes — Confirm We Pre-Frame Your Close →","trg-ds-yes")
    P.raw('<hr>')
    P.h2("We Help You Close",eyebrow="★ BEST OPTION — The whole closing system")
    P.raw('<p class="price">Regular Price: <s>$97 one-time</s><br>Yours today: <b class="big nobreak">Just add $20</b> more, one-time<small>($47 total)</small></p>')
    P.p("Everything you need from the moment you pull up to the curb to the moment they sign.")
    P.p("**The First Impression Protocol**\nHow to show up, knock, introduce yourself, and walk the property so you are stacking micro yeses before a single word about price is spoken.",
        "**The Price Frame**\nOne sentence that sets the expectation before the number comes out, so it lands as confidence instead of sticker shock.",
        "**The Competitor Pre-Frame Script**\nWhat to say the moment a homeowner mentions other painters are coming out to quote. Works by phone, text, or in person.",
        "**The Estimate Close Card**\nExact words for the three moments that kill more estimates than anything else. “I need to think about it.” The spouse wasn't home. “Can you do any better on price?” All three handled in under 60 seconds each. Print it, laminate it, bring it to every estimate.",
        "**The 90-Day Cold Lead Follow-Up Sequence**\nOne message per week for 12 weeks, written for SMS and Messenger. For every lead that went quiet after the first two contacts. Most painters give up after two texts. The job that replies on week nine is money they would have left on the table.")
    P.p("**Everything included:**")
    P.chk(["First Impression Protocol — how to show up and stack micro yeses before you quote","Price Frame — one sentence that makes the number land right","Competitor Pre-Frame Script — sets you up before anyone else arrives","Estimate Close Card — three objections, three answers, laminate-ready","90-Day Cold Lead Follow-Up Sequence — 12 weekly messages, SMS and Messenger ready",
           "**FREE:** 1-Hour Private Coaching Call with Lanty (stacks with previous calls) — book it in your first 30 days."])
    P.p("One extra closed estimate this month covers this pack a hundred times over.")
    P.btn("Yes — Confirm We Help You Close →","trg-oto-yes")
    P.decline("❌ No thanks — I'll try to figure out my own sales process alone","(even if it takes months and costs thousands in unclosed jobs)")
    P.h2("Once We Help You Close Is In Your Hands — Here's What Changes",eyebrow="Picture it")
    P.ul(["You show up to every estimate knowing exactly what to do before you knock — and the homeowner is already leaning toward yes before the number comes out.",
          "The moment a homeowner mentions other painters are quoting, you have one sentence ready that makes you the reference point before anyone else shows up.",
          "You stop winging the three hardest moments at the table. “I need to think about it” no longer ends the conversation. Neither does the absent spouse or the competing quote.",
          "Leads that went quiet after the first two texts stop being dead leads. Week nine of the follow-up sequence has booked jobs that looked gone for two months.",
          "Your close rate on residential estimates goes up — not because your work got better, but because the decision was already forming in your favor before you sat down."])
    P.h2("Still Deciding Between The Two?",eyebrow="For just $20 more")
    P.p("Here is what $20 more actually buys you.",
        "**Option 1 — We Pre-Frame Your Close · $27**\nGives you one script. It handles the moment another painter is in the picture. Everything else at the estimate is still on you.",
        "**Option 2 — We Help You Close · $47**\nGives you all five tools. The approach, the frame, the pre-frame, the close card, and 12 weeks of follow-up for every lead that went quiet.",
        "Here is what it would cost to put those pieces together yourself:")
    P.ul(["A sales trainer or closer coach for one session — **$150–500/hr**","A copywriter to write a 12-week SMS follow-up sequence — **$300–800**","Your own time researching and scripting the objection handlers — **+ your hourly rate**"])
    P.box("**$450+** to build the same five tools separately.\nOr **$47** to have all of them today.",red=True)
    P.p("For $20 more — you are not choosing between two scripts.",
        "You are choosing between one tool and a complete closing system.",
        "If you went with We Pre-Frame Your Close and want to upgrade later, you can do it at any time for the $20 difference. The door stays open.",
        "But the time to make the call is right now, while you are already here.")
    P.btn("Upgrade to We Help You Close →","trg-oto-yes")
    P.decline("❌ No thanks — I'll try to figure out my own sales process alone","(even if it takes months and costs thousands in unclosed jobs)")
    P.h2("This Is The Last Piece.")
    P.ol(["The leads are coming in. The appointments are booked. Everything upstream is handled.","This is what happens when you're standing in front of them."])
    P.p("Most painters lose jobs they already had. Not because the work wasn't good. Not because the price was wrong.",
        "But because nobody ever gave them the words, the frame, or the approach that turns a homeowner who's already interested into one who signs on the spot.",
        "One option gives you the single script that positions you before anyone else arrives.",
        "The other hands you the whole system — from the moment you pull up to the curb to the follow-up message nine weeks after they went quiet.",
        "One extra closed job covers either one completely.",
        "Pick the one that fits where you are right now. Then go close something.")
    P.decline("❌ No thanks — I'll try to figure out my own sales process alone","(even if it takes months and costs thousands in unclosed jobs)")
    P.fine(support=False)
    return P

# ---------------------------------------------------------------- OTO 4 (Easy Start)
def oto4():
    P=Page()
    P.kicker("The Easy Start · Before you go")
    P.h1("Still Here.")
    P.p("This page only shows up for one reason.",
        "You're still here because something on this page is still pulling at you.")
    P.h2("You Said No To A Full Calendar. You Said No To 15–20 Confirmed Estimates A Month. You Said No To Never Chasing A Lead Again.")
    P.p("**Which means…**")
    P.ul(["You said no to finishing the job and coming home without checking your phone every 20 minutes wondering if anyone called back.",
          "You said no to your wife seeing you actually present at dinner instead of calculating whether next month's pipeline is enough.",
          "You said no to being the painter in your market who's booked three weeks out while everyone else is scraping.",
          "You said no to the business that runs while you paint — instead of the business that only runs when you chase it."])
    P.p("You said no to time.\nYou said no to margin.\nYou said no to the version of this that looks like what you actually got into business for.",
        "But here's what I know.",
        "You didn't say no to any of that because you don't want it.",
        "You said no because **$497 felt like too much before you'd seen it work.**",
        "That's the only reason.",
        "So here's what we're going to do.",
        "We're going to remove that reason completely — and stack everything else on top so saying no becomes genuinely hard to justify.")
    P.h2("Start At $247 A Month For The First Two Months.",eyebrow="The Easy Start")
    P.box("**MONTHS 1–2: $247 per month**\n**FROM MONTH 3: $497 per month**",red=True)
    P.p("Same ads. Same team following up every lead within five minutes. Same confirmed estimates booked straight into your calendar while you're on a job. Same Profits Vault — all 10 modules — yours on Day 1, kept permanently. Same free 1-hour coaching call with Lanty in your first 30 days.",
        "The exact same thing as We Get You Booked.",
        "Every single piece of it.",
        "Just half the price while you watch it work.",
        "From month three — when the estimates are landing and the calendar is filling — it moves to $497. Not because anything changes on our end. Because by then the results will have already made the number feel small.",
        "And because you're still here — we're adding everything else in.")
    P.h2("Here's Everything That Comes With It.",eyebrow="When you take the Easy Start today")
    P.p("**1. We Get You Booked — Full Done-For-You** *(Value: $497/mo)*\nAd built and live within 48 hours. Every lead followed up within 5 minutes. Confirmed estimates in your Google Calendar. Weekly reporting. The whole machine running while you paint.",
        "**2. The Profits Vault — 10-Module Training** *(Value: $297)*\nThe full business side of painting. Job costing, closing, crew structure, cash flow, reading your numbers. Yours on Day 1. Kept permanently even if you leave.",
        "**3. We Build Your Funnel — Landing Page + 90 Days of Posts** *(Value: $197)*\nYour landing page built and live within 48 hours. One link for every platform — Facebook, Instagram, Nextdoor, anywhere you post. Plus 90 days of copy-paste posts already written for a painting contractor, organized by week, ready to drop into every platform daily.",
        "**4. We Help You Close — Full Closing Toolkit** *(Value: $47)*\nThe First Impression Protocol — how to show up and stack micro yeses before you quote. The Price Frame — one sentence that makes the number land right. The Competitor Pre-Frame Script — sets you up before any other painter arrives. The Estimate Close Card — exact words for the three objections that kill most estimates. The 90-Day Cold Lead Follow-Up Sequence — 12 weekly messages for leads that went quiet.",
        "**5. FREE: 1-Hour Private Coaching Call with Lanty** *(Value: $500)*\nYour market, your numbers, your close rate — Lanty walks through all of it with you directly. Book it in your first 30 days.")
    P.box("**Total Value: $1,538+**\n**Your Price Today: $247/mo** for months 1–2, then $497/mo from month 3",red=True)
    P.h2("Here's What $247 Actually Means In Real Terms.",eyebrow="The math")
    P.ol(["One confirmed estimate.","One closed job. $3,500 average."])
    P.p("**Result:** One job in your first month covers the retainer for the next 14 months.",
        "You're not betting $247 on us.",
        "You're betting $247 on yourself — that you can close one job from a confirmed estimate sitting in your calendar.",
        "You can. That's why you're still reading.")
    P.h2("We Get You Booked — Easy Start",eyebrow="One choice. Last door.")
    P.raw('<p class="price">Months 1–2: <b class="big">$247</b> /mo<small>Then $497/mo from month 3.</small></p>')
    P.chk(["Full done-for-you — ads, follow-up, calendar booking","The Profits Vault — 10 modules, yours permanently","Landing page built and live within 48 hours","90 days of copy-paste posts — organized by week, cross-platform ready","First Impression Protocol — how to show up and stack micro yeses","Price Frame — one sentence that makes the number land right","Competitor Pre-Frame Script — sets you up before anyone else arrives","Estimate Close Card — three objections, three answers","90-Day Cold Lead Follow-Up Sequence — 12 weekly messages","**FREE:** 1-Hour Private Coaching Call with Lanty"])
    P.p("*This offer exists on this page only. It won't appear anywhere else in this funnel and it won't be available after you leave this page.*")
    P.btn("Yes — Lock In The Easy Start Rate →","trg-oto-yes")
    NO4=("❌ No thanks — I've said no to leads, no to a page that catches them, no to closing them at the estimate, and no to the easy start. I'll figure it out from scratch on my own.","")
    P.decline(*NO4)
    P.h2("Two Months From Now, One Of Two Things Is True.")
    P.p("**One:** Your calendar has confirmed estimates you didn't have to chase. You're home for dinner without the pipeline math running in your head. The landing page is live. The posts are running. The close card is laminated in your truck. The business is doing what you built it to do.",
        "**Or:** It looks exactly like today.",
        "The first one costs $247 to find out.",
        "The second one costs nothing — except every job, every estimate, every slow month that calendar would have fixed.",
        "This is the last time this offer appears.",
        "The decision is yours.")
    P.decline(*NO4)
    P.fine(support=False)
    return P

# ---------------------------------------------------------------- Thank-you pages
def _ty(call):
    P=Page()
    P.kicker("Order confirmed")
    P.h1("You're in. Take a breath.")
    P.p("What you just did matters more than you think.")
    P.h2("Welcome To The Other Side.")
    P.p("The painters who figure this out look back and say the same thing:",)
    P.quote("“I wish I did this sooner.”")
    P.p("Most painters spend years doing it the hard way.",
        "Chasing leads that go cold.\nDriving to estimates they lose at the table.\nWatching the slow months come around like clockwork.\nHoping this time it's different.",
        "You just made the decision that changes all of that.",
        "Not someday. Starting this week.",
        "Everything you put in place today — the Playbook, the posts, the page, the follow-up, the close — is about to start working for you.",
        "**Not** because it's complicated. **But** because it's already built. All you have to do is use it.",
        "The hardest part is already behind you.",
        "You made the right call.")
    P.h2("Here's Exactly What Happens From This Moment Forward.",eyebrow="What happens next")
    P.h3("Step 1 — Check Your Inbox Right Now")
    P.p("An email is on its way to you from us.",
        "When it arrives — star it, mark it as important, and reply to it. This tells your email provider we're not spam and makes sure nothing we send you ever gets buried.",
        "Also check your spam or promotions folder right now. If you see anything from us in there, move it to your inbox and mark it as not spam. Everything we're about to send you lives in your email.")
    P.h3("Step 2 — Open Your Access Email")
    P.p("Within the next few minutes you'll receive your access email with everything you purchased today.",
        "Your Super Paint Close Playbook arrives immediately. Open it tonight. Your first post is on page one and takes under a minute to use.",
        "Starting tomorrow morning — and every morning for the next 7 days — one bonus PDF from your 7-Day Fast Start Kit lands in your inbox. Each one is one page, built for one specific moment you'll hit in your first week. Open it, read it, use it that day. That's it.")
    P.h3("Step 3 — Watch For Your Custom Setup Email")
    P.p("If you added anything to your order that we build for you — a landing page, a Facebook ad, a Messenger setup — you'll receive a separate onboarding email within 24 hours with a short form to fill out.",
        "That form is how we collect everything we need to get your custom deliverables built and live.",
        "Fill it out the moment it arrives. The faster it comes back to us, the faster everything goes live for you.",
        "**Here's what to expect based on what you ordered:**")
    P.box("📋 **If you ordered We Get You Booked or We Get You Leads**\nOnboarding form incoming. We'll collect your service area, ad account access, and calendar link. Your ad goes live within 48 hours of us receiving that form.")
    P.box("📋 **If you ordered We Build Your Funnel or We Build Your Page**\nOnboarding form incoming. We'll collect your domain and hosting access. Your landing page goes live within 48 hours of us receiving that form.")
    P.box("📋 **If you ordered We Help You Close or We Pre-Frame Your Close**\nEverything is in your access email already. Open it, read it, and use it before your next lead comes in or your next post goes out.")
    if call:
        P.h2("Your Free 1-Hour Coaching Call With Lanty",eyebrow="🎁 Included with your order")
        P.p("This is included with your order today.",
            "Bring your market, your numbers, your close rate, your biggest bottleneck — whatever is sitting between you and a full calendar right now. Lanty walks through all of it with you directly.",
            "Most painters pay $500 for a call like this. Yours is free. Available for the next 30 days.",
            "And here's something else.",
            "If there was anything on this page today that you passed on — the landing page, the ad setup, the follow-up tools, the closer pack — bring it up on the call.",
            "Lanty can walk you through exactly which one makes the most sense for where you are right now, and if it's a good fit, he'll get you in at a special rate you won't find anywhere else in this funnel.",
            "The call is free. The conversation costs you nothing. And it might be the most valuable 60 minutes you spend on your business this year.",
            "Book it before the 30 days runs out.")
        P.btn("Book Your Free Call With Lanty →",href="BOOKING-CALENDAR-URL")
    P.h2("Your Action List For The Next 10 Minutes:",eyebrow="Don't freeze up")
    items=["**Check your inbox** — your access email is on the way","**Check spam** — move anything from us to your inbox right now","**Star and reply to our first email** — keeps us out of spam permanently","**Open the Playbook the moment it arrives** — your first post is on page one"]
    if call: items.append("**Book your free call with Lanty** — link is right above this")
    P.chk(items)
    P.h2("You're One Step Away From The First Lead Coming In.")
    P.p("Not a maybe lead. Not a shared lead that three other painters got at the same time.",
        "A homeowner in your neighborhood — your market — who saw your post, clicked your link, filled out your form, and is waiting for you to call.",
        "That's what's on the other side of the next 48 hours.",
        "We built this for painting contractors who are done leaving jobs on the table.",
        "You just proved you're one of them.",
        "Let's get to work.",
        "— Lanty & The Super Paint Close Team")
    P.fine()
    return P

def ty_call(): return _ty(True)
def ty_only(): return _ty(False)
