### HOME
> Everybody complains about the weather, but nobody every does anything about it.  Except him - he never complains about the weather.

-- David Mamet, "Squirrels"

Substitute "documentation" for "weather" and you get a pretty good description of "the documentation problem" in software development culture.  Everybody laments the dearth of good documentation, but very few do much of anything about it.  Spotty documentation seems to be endemic to software, especially open source software.  On the other hand, who is to say what counts as "good", or even "adequate" documentation?  What experts find adequate beginners may find useless, and what beginners find wonderfully helpful experts may find annoying.

The primary purpose of the Code Genres project is to explore the nature of technical (specifically software) documentation and its relationship to code, computation, etc..  A secondary goal is to generate specific tools and techniques in the service of good software documentation.

* [Overview](overview)
* [Some quotations](Quotations)
* [Rethinking Literate Programming](Rethinking-Literate-Programming)
* [Code Lit](Code-Lit) Some literary concepts applied to programming texts
* [The Meanings of Code:  Denotationism and Expressivism](Meanings-of-Code)
* [Philology and Hermeneutics: the Art and Science of Reading Code](Philology-and-Hermeneutics)
* [Code Exegesis](Exegesis): Naming, Describing, Explaining
* [Roles and Requirements](Roles-and-Requirements)  Who are the consumers of code and documentation, and what do they want?
* [On Documentation](On-Documentation)
* [Tests as Documentation](Tests-as-Documentation)
* [Resources](resources)

### OVERVIEW

# The Concept of Code Genres

The notion of "code genre" is taken from [Mikhail Bakhtin](http://en.wikipedia.org/wiki/Mikhail_Bakhtin)'s small masterpiece "The Problem of Speech Genres".  The concept of genre comes from literary studies; examples of literary genres include Greek Tragedy, the Epic, the [Petrarchan Sonnet](http://en.wikipedia.org/wiki/Petrarchan_sonnet), and Elegy.  Less lofty literary genres include the nursery rhyme, the limerick, and the newspaper article.

But the concept of genre extends far beyond such well-known exemplars.  Very roughly speaking, a genre is characterized by a set of norms (aka "traditions") governing the form of "instantiations" of the genre.  Thus even such humble literary productions as the shopping list, the traffic ticket, and school report card can be viewed as genres.  Bakhtin's brilliant essay applied the concept of genre to speech performances of all kinds: not only those with a recognizable genre, such as political speeches and theatrical performances, but even the most mundane and routine speech performances, such as greetings, military commands, and ordering food in a restaurant.  In order to be recognized _as_ performances of a certain kind, they must conform to the norms of the genre: a military command that is offered with a whimper and a "please?" would just confuse the troops, since what counts as a command (in the military) is determined by certain syntactic forms (imperative mood, no "please") as well as non-verbal form - a firm tone, etc.

The concept of _code genre_ builds on these notions.  The various forms of documentation - the User Guide, the Technical Reference Manual, the Tutorial, etc. - are easily construed as literary genres: their form is governed by a set of norms (conventions, expectations, etc.) that has emerged gradually in the course of the history of computation.  Those norms may be relatively loose, but they are norms nonetheless.

But _code itself is a kind of literary genre_.  Programs have certain characteristic forms; these forms are only partially determined by the formal syntax of the language.  For example, norms have emerged governing the naming of certain classes of variables; the paradigmatic case is the use if _i_ as the name of an index variable used for looping.

### QUOTATIONS

# Quotations

You can find lots of quotations about LP at [literateprogramming.com](http://www.literateprogramming.com/).

LP = "Literate Programming", by Donald E. Knuth, Center for the Study of Language and Information, 1992

## Knuth

From the essay "Literate Programming", in LP:

> "Let us change our traditional attitude to the construction of programs.  Instead of imagining that our main task is to instruct a *computer* what to do, let us concentrate rather on explaining to *human beings* what we want a computer to do." (p. 99)

> "The practitioner of literate programming can be regarded as an essayist, whose main concern is with exposition and excellence of style.  Such an author, with thesaurus in hand, chooses the names of variables carefully and explains what each variable means.  He or she strives for a program that is comprehensible because its concepts have been introduced in an order that is best for human understanding, using a mixture of formal and informal methods that nicely reinforce each other." (p. 99)

> "In fact, my enthusiasm is so great that I must warn the reader to discount much of what I shall  say as the ravings of a fanatic who thinks he has just seen a great light." (p. 100)

> "I must confess that there may also be a bit of malice in my choice of a title.  During the 1970s I was coerced like everybody else into adopting the ideas of structured programming, because I couldn't bear to be found guilty of writing *unstructured* programs.  Now I have a chance to get even.  By coining the phrase "literate programming," I am imposing a moral commitment on everyone who hears the term; surely nobody wants to admit of writing an *illiterate* program". (p. 100)

> "...I think that a complex piece of software is, indeed, best regarded as a *web* that has been delicately pieced together from simple materials... If we express a program as a web of ideas, we can emphasize its structural properties in a natural and satisfying way." (p. 101)

> "Literature of the program genre is performable by machines, but that is not its main purpose.  The computer programs that are truly beautiful, useful, and profitable must be readable by people.  So we ought to address them to people, not machines."  DEKnuth, Preface to LP, p. ix.

"Computer Programming as an Art" (1974), in LP pp. 1-16:

> "When I speak about computer programming as an art, I am thinking primarily of it as an art *form*, in an aesthetic sense.  The chief goal of my work as educator and author is to help people learn how to write *beautiful programs*." (p. 7)

> "Some programs are elegant, some are exquisite, some are sparkling.  My claim is that it is possible to write *grand* programs, *noble* programs, truly *magnificent* ones!" (p. 8)

"How to Read a WEB" (1986), in LP pp. 179-184:

> "A WEB program is a Pascal program that has been cut up into pieces and rearranged into an order that is easier for a human being to understand... In other words, WEB programs and Pascal programs are essentially the same kinds of things, but their parts are arranged differently." (p. 179)

"Mathematical Writing" (1987), in LP pp. 235-241.  MW consists of class notes written by Paul Roberts from a course taught by Knuth in 1987, but since Knuth included it in LP we can assume he endorses it.

> "The guiding principle behind WEB is that each module is introduced at the psychologically right moment." (p. 236)

> "Don himself always felt it was quite clear what had to be presented next, throughout the entire composition of this huge program [i.e. TeX - GR].  There was at all points a natural order of exposition, and it seems that the natural orderings for reading and writing are very much the same." (p. 236)

> "In WEB we are not constrained by top-down, bottom-up, or any other order." (p. 238)

## Other LP quotations

> "Under the literate programming paradigm, the central activity of programming becomes that of conveying meaning to other intelligent beings rather than merely convincing the computer to behave in a particular way. It is the difference between performing and exposing a magic trick." Ross Williams, FunnelWeb Tutorial Manual p 4 (quoted at [literateprogramming.com](http://www.literateprogramming.com/))

# Inferential Semantics

a/k/a Inferential Role Semantics.  Broadly speaking, inferential semantics is a (foundational) approach to explaining meanings in terms of inference; it stands in contrast to representational semantics, which explains meaning in terms of representation.  Inferentialism says that the content of a concept is determined by its inferential articulation, the network of inferences in which it plays the role of premise or conclusion.  What gives "the triangle is crimson" its meaning is its relation to other statements like "the triangle is not green" and "the triangle is red".  Representationalism says that the content of a concept is determined by its referential relation to the world; what makes "the triangle is red" meaningful is the representational relation between the word "red" and the redness of the triangle.

The relevance here has to do with the idea that a program is a web of concepts.

See "Semantic Inferentialism and Logical Expressivism", in "Articulating Reasons: An Introduction to Inferentialism", by Robert Brandom, Harvard University Press, 2000.

### RETHINKING LITERATE PROGRAMMING

>[Feynman's Problem-Solving Algorithm](http://drtomcrick.com/2011/04/26/feynman-problem-solving-algorithm/):  1. Write down the problem.  2.  Think very hard.  3.  Write down the answer.

**NB** This is a semi-organized, incomplete draft.  I'm working out some lines of argument; currently most of them seem to hold together reasonably well, but if you see a flaw let me know.  I don't want this page to be a debating forum, but I do want to do justice to all sides of the issues; the goal is to explicate, not dominate.  References to LP are to Knuth's essay "Literate Programming", in his book of the same name, published in 1992 by CSLI.

> "I must confess that there may also be a little bit of malice in my choice of a title.... By coining the phrase "literate programming," I am imposing a moral commitment on everyone who hears the term; surely nobody wants to admit writing an _illiterate_ program.  - DE Knuth (LP, p. 100)

But it's not a very useful label, since all program texts are a form of literature.  Some alternative suggestions are offered below; at the very least we should always prefer "Knuthian Literate Programming" to plain "Literate Programming".

# Preliminaries

## Programming Styles

In order to demarcate literate programming we need a way to refer to whatever it is that is not literate programming.  Caveat: we're talking about styles here.  Knuth refers to LP as a method, but it's really just a style, not a rule or set of rules that tell you what to do.

### Dragnet Programming

> "Just the facts, ma'am."  -- Detective Joe Friday

A/K/A minimalist programming.  Just the code, no comments, no documentation.

For those who did not grow up watching 1960s American television, [Dragnet](http://en.wikipedia.org/wiki/Dragnet_(series)) was a popular weekly police drama whose "action" largely centered on interviewing of witnesses and interrogation of suspects.  The suspects almost inevitably confessed, and the witnesses routinely went off on tangents, compelling our heroes, Detective Joe Friday and his partner Bill Gannon, to gently but firmly remonstrate "Just the facts, ma'am".  The show started out on radio, and you can find episodes of it on the internet; the dialog is amusing, very stylized, like it just stepped out of a pulp novel.

### Common Programming

Common programs are composed of programming language code decorated by comments.  The "natural" order of composition is: code, comment, repeat.  The order of presentation is determined by the sequential organization of the text in its storage unit (virtually always a file): readers accesses program text using a text editor, and virtually all text editors present file contents "top to bottom".  The order of reading is free; most text editors provide facilities that allow the reader to skip around within the text at will.

Other possibly identifiable styles:

* Elliptic programming
* [Gnomic](http://en.wiktionary.org/wiki/gnomic) programming

### Exegetical Programming

The genus of which literate programming is a species.  Lots of comments, explanatory documentation, etc.

Other possible candidates to replace "literate programming":

* Narrative programming - writing doco and code as if writing an essay
* Talmudic programming

### Paraprogramming

> "A literary work consists, entirely or essentially, of a text, defined (very minimally) as a more or less long sequence of verbal statements that are more or less endowed with significance.  But this text is rarely presented in an unadorned state, unreinforced and unaccompanied by a certain number of verbal or other productions, such as an author's name, a title, a preface, illustrations.  And although we do not always know whether these productions are to be regarded as belonging to the text, in any case they surround it and extend it, precisely in order to _present_ it, in the usual sense of this verb but also in the strongest sense: to _make present_, to ensure the text's presence in the world, its "reception" and consumption in the form (nowadays, at least) of a book.  These accompanying productions, which vary in extent and appearance, constitute what I have called elsewhere the work's _paratext_.... [T]he paratext is what enables a text to become a book and to be offered as such to its readers and, more generally, to the public.  More than a boundary or a sealed border, the paratext is, rather, a _threshold_, or - a word Borges used apropos of a preface - a "vestibule" that offers the world at large the possibility of either stepping inside or turning back.  It is the "undefined zone" between the inside and the outside, a zone without any hard and fast boundary on either the inward side (turned toward the text) or the outward side (turned toward the world's discourse about the text), an edge, or, as Phillippe Lejeune put it, "a fringe of the printed text which in reality controls one's whole reading of the text.  Indeed, this fringe, always the conveyor of a commentary that is authorial or more or less legitimated by the author, constitutes a zone between text and off-text, a zone not only of transition but also of _transaction_: a privileged place of a pragmatics and a strategy, of an influence on the public, and influence that - whether well or poorly understood and achieved - is at the service of a better reception for the text and a more pertinent reading of it (more pertinent, of course in the eyes of the author and his allies)." - Gerard Genette, "Paratexts: Thresholds of Interpretation", Cambridge University Press 1997, p. 1-2

A connection to KLP should be fairly obvious. Take the code part of a LP production as the text, and the explanatory, narrative prose part as paratext - it's purpose is, as Knuth said more than once, is to present the code in an order and form best fit to the psychology of the reader, or in Genette's terminology, to maximize the "reception" of the text.

On the other hand, Genette does not treat commentary as paratext, but he does have a chapter on the "note", which he describes as "a statement of variable length (one word is enough) connected to a more or less definite segment of text and either placed opposite or keyed to this segment."  (p. 319)
# Program Text Properties

## Ordering

Various orderings are associated with program texts:

* Execution order
* Composition order
  * Temporal order in which the code was written
  * Arrangement of finished code within and across files
* Presentation order
* Reading order

## Function, Algorithm, Code

> LP is about documentation (among, perhaps, other things).  So a critical question is what counts as documentation?  "Self-documenting code" is just code without comments or documentation; what makes it "self-documenting"?  In the case of functions (procedures) this leads to questions about the nature of algorithms, functions, and code text.

### Algorithm

An algorithm is a procedure.  Mathematically, algorithms are abstract, mathematical objects.  To express an algorithm, you have to pick a formal language and write it down.  What you write down may be said to _denote_ the algorithm, or to _express_ it.  Denotation and expression are distinct concepts.  Either way, the critical point is that algorithms are pure procedure, and written representations of algorithms are pure syntax.  The names involved in the written form have no intrinsic meaning; they are merely blobs of syntax.  So what expresses the algorithm is pure form, to the express exclusion of any meanings suggested by possible natural language interpretations of the names used.

> It follows that the "self-documenting" character of code involves two distinct notions.  The structure of the code itself may be thought of as a form of "documentation" of the algorithm it implements, but that's a bit of a stretch, since in some sense that structure _is_ the algorithm.  Saying that the code documents the algorithm is a bit like say that tokens document their types, which is not something we would ordinarily say.  We want documentation to _explain_, and tokens do not explain their types, they only instantiate them.  On the other hand - and this is Knuth's point - the names used in the code can be used to "document" the concept of the algorithm for humans.  But here again there is (arguably) no genuine explanation going on, only a kind of hand-waving.  Calling a variable "widget-count" doesn't really explain anything.  It remains up to the reader to concoct an explanation based on the names and the algorithm structure.

### Code

The code that expresses an algorithm is one "instantiation" of the abstract object.  For any algorithm and any (ordinary) programming language, there are an infinite (or at least large) number of ways to write it down.  All you need to do is change the variable names and you get a distinct expression of the same algorithm.

### Function

Algorithms (always?) implement functions.  Whether or not any given function can be implemented as an algorithm is a nice question we won't go into here.  Suffice it to say that the functions we are interested in for programming purposes can be implemented as algorithms.  But there may be many distinct algorithms that implement the same function; and, as just mentioned, there are always many ways to write down a given algorithm.

There are many ways to think about functions, even to define what a function is.  There are at least three fundamental approaches, corresponding to the the three major foundational frameworks for mathematics:

* Set theory.  A set theoretic function is a set of ordered pairs, often call a graph.  We can distinguish between a function and its graph; in set theory, a function just _is_ its graph.  The set theoretic concept of function is non-computational.
* Category theory.  [TODO: borrow from [Goldblatt's](http://ebooks.library.cornell.edu/cgi/t/text/text-idx?c=math;idno=gold010) wonderful exposition of the CT notion of function.]
* Type theory is a new and very recent entrant in the foundations-of-mathematics sweepstakes; see [HoTT](http://homotopytypetheory.org/book/).  Actually there are many type theories; HoTT uses type theory in combination with Homotopy Theory to come up with a foundation for mathematics (it's over my head, but it's fascinating).  Type theoretic notions of "function" are intrinsically computational.

The set-theoretic concept of a function is non-computational, but it is nonetheless extremely useful for expressing the meanings of functions, even if you prefer some other notion of what functions are.  In fact this can be viewed as an advantage of the set-theoretic approach: it allows us to express function concepts without getting bogged down in algorithm details.

The relevance to documentation (and LP) is that self-documenting functions document algorithms, and it is useful to make a conceptual distinction between function and algorithm.  This leads to the idea that a good way to document an algorithm is to _specify_ the function it implements in set-theoretic, non-procedural notation.  Such a specification would convey the "meaning" of the function in the abstract.  The assumption is that this would be easy to read (or at least easier to read than the implementation code), and would tell the reader what the implementation code is supposed to be doing.  In the ideal case, no further documentation would be needed.

> Where I'm going with this: instead of improving the readability/understandability of code by adding natural language documentation etc. we should think about supporting a formal specification language.  I'm thinking specifically about the [Z Specification Notation](http://en.wikipedia.org/wiki/Z_notation), which is a formally designed notation based on straightforward set theory.  It also has a formally defined semantics, which means that in principle specifications written in Z can be automatically checked for consistency.

## Expressivity

# Literate Programming

## Knuthian Literate Programming (KLP)

[I started out wanting a more precise idea of what KLP _is_, but quickly realized that that is the wrong question.  There is no fact of the matter, nothing in the world that can settle for us what KLP is and is not.  So the better question addresses the role of the term "literate programming" in the doings and sayings of programmers.  So here is a list of characteristics that are commonly associated with the term, taken mostly from Knuth's work "Literate Programming".

* Monolithic composition.  This is one of the two major characteristics of Knuthian LP (the other being free order).  Exegesis and code go in the same file.
* Inversion of the normal "order of composition" - instead of adding exegesis to code, KLP adds code to exegesis.
* Bilingualism - KLP texts are bilingual.  They contain "code" - text written in a programming language - as well as exegesis - text written in English or some other natural language.  Actually it would be more accurate to say that litprog texts are trilingual - the exegesis is written in some form of markup language (XML, LaTeX, Markdown, etc.) that combines a formal syntax and informal prose.
* Linear, narratively structured code - KLP intentionally violates the syntactic rules of the target programming language by supporting the decomposition and rearrangement of code sequences.  (So the bilingualism of KLP is actually a kind of meta-bilingualism; you don't really write code according to the rules of the target language, you write it according to KLP rules, which the KLP system then analyzes and reassembles into a legal text in the programming language.)
* A fundamentally rhetorical view of "the art of computer programming".  Knuth makes a big deal out of the idea of writing programs for human readers, by which he apparently means programs that answer to the psychological needs and limitations of human readers (he's explicit on the psychological bit).  The tension between this (which is unavoidably a matter of rhetoric) and writing code that the machine can "understand" is beyond obvious; machines do not have a psychology and are immune to rhetorical tricks.  But strangely enough Knuth says almost nothing about it.
* etc.

So if you had to define LP, you'd probably say something like: monolithic source files containing both extensive narrative documentation and code, with free order for code so that the order of presentation of documentation and code is psychologically optimal.

### Presuppositions

1. The proper _order_ of presentation of a program text is linear; by implication, the proper order of reading is front-to-back, start-to-finish.
2. The proper _mode_ of presentation is narrative.  Program texts should be like literary essays, composed of smoothly flowing English narrative running from a beginning to an end.  The code proper, written in a formally defined programming language, is a kind of add-on, provided (out of mercy?) to help the computer understand the narrative.

These presuppositions are highly debatable.

### Order of Presentation and Reading

Presupposition 1 is a very bold hypothesis, and is almost certainly too strong, if not outright wrong.  Algorithms do have a natural order; by definition, an algorithm is a sequence of steps, so the natural thing to do is present (and read) them by starting with step 1 and proceeding to the last step.  But even this is a little too strong; algorithms have branches and loops, and so may have many different execution paths, one for each input.  It follows that, if we insist on finding the One True Order of presentation and reading of an algorithm, we are forced to concede that it depends on the input.  But it is surely a mistake to think that the logical structure of an algorithm should determine the order of reading.  Reading text -- whether formal code or informal natural language - is a psychological activity, not a logical one.  The order of reading of an algorithm, for any particular reader, is an empirical matter; if we wanted to know which order is most common, we would have to conduct a study involving eye tracking and various other techniques drawn from psychological research.  

Knuth would probably agree with this much, I suspect.  In fact one of the primary virtues of the LP "method", for him, is just that it allows authors the freedom to order code in any way they see fit.  This includes presenting the steps of an algorithm in an order that deviates from its execution order.  The justification for doing so is psychological: the program should be presented in the order that best fits the psychology of reading (understanding) the code, which may be at odds with the order of execution.  The obvious problem is that we simply do not know what ought to count as "best" or "most natural" order; indeed we cannot know this, since there is no such beast.  Knuth's remarks regarding the "best" order of presentation reflect fundamentally personal psychological and aesthetic commitments that others may not share.  So the argument he makes on behalf of KLP - that it leads to "better" code, etc. - has no _principled_ justification.

On the other hand, we have lots of enthusiastic positive testimony from people who have used KLP techniques.  I think the appropriate response is "better compared to what"?  The counter-argument is based on the observation the KLP is a thing of its time, closely tied to the state of programming language design in the late 1970s and 1980s.  Programming language design has not evolved in the direction of KLP, but it has evolved, and (in my view) is moving in a direction that renders KLP unnecessary (and possibly harmful).  

> More on this below; briefly, the argument is that programming languages are becoming so expressive that (eventually, maybe) no comments will be needed.  The holy grail is not a linear, narrative language that can express algorithms, but a formal notation so powerful that you can say what you need to say _clearly_ in the notation alone, dispensing with the need for exegesis (except for pedagogical purposes, of course).

So much for algorithms under KLP.  But even if we could empirically determine some "best" (or most common) order of presentation for algorithms, virtually all useful programs consist of multiple algorithms, and my guess is that most "programs" have no natural starting or ending point.  Applications have a starting point (usually some variation on "main"), but no natural ending point.  Many (most?) libraries have neither.

Knuth surely knew this, as any programmer would.  That may explain why in his LP writing he stresses order of _presentation_ rather than order of composition, execution, or the like.  To a large extent, he seems to have viewed his main early LP tool ("WEB") as a device for remedying deficiencies in Pascal (as he explicitly hinted in [citation here]).  He did not explicitly say (so far as I know) that lack of support for a linear, narrative order (with out-of-line chunks of procedures) counts as a deficiency of Pascal, but the conclusion seems inevitable.  Follow this line of thought to its logical conclusion, and you end up with an implicit norm for programming language and tool design: a well-designed programming language would help (force?) the programmer (author) to compose (and think?) programs in a linear, narrative form, and editors and other tools would present texts in similar form (along with pleasing typesetting, cross-references, indices, and the rest of the KLP apparatus).  This has obviously not happened.

So there is an obvious tension between the underlying (and clearly _normative_) presuppositions of KLP and the way things actually work, which helps to explain why programming languages have not evolved in the direction of KLP.

### Mode of Presentation

> TODO: Knuth's model for program text is the essay, read from beginning to end.  I think a better model is the [Commonplace Book](http://en.wikipedia.org/wiki/Commonplace_book), which is a collection of stuff and need not be read in any particular order.  For a modern exemplar, consider [The Book of Lists](http://en.wikipedia.org/wiki/The_Book_of_Lists); the fun of it is that you can turn to any page and read a list.

### Expressiveness

Knuth urges that "[t]he practitioner of literate programming can be regarded as an essayist, whose main concern is with exposition and excellence and style." (LP p. 99)

But a program is not an essay; there is a radical difference between the two.  Essays are primarily _expressive_; they convey the thoughts, beliefs, attitudes, etc. of the author.  Code (text written in a formal language, with a stipulated semantics) is not like this.  The primary expressive function of code is to express algorithms, not authors.  Coders can use variable names to suggest intended interpretations of the data and functions involved, and to some extent at least these reflect authorial intentions.  But they are secondary, and they may be misleading or just plain wrong.

One way of looking at this distinction is in terms of laws versus norms.  What program code expresses is law.  Machines do as they are told because they have no choice in the matter, any more than a hurled stone has a choice regarding its path and velocity.  The program code lays down the law.  Not natural law, of course; merely local law, specific to the rules of the language.  But those rules are laws, which establish a form of necessity: a program correctly written in, say, Java, _necessarily_ compiles.  An incorrectly written program, one that violates the laws of the language, is no program at all.

By contrast, essays can be judged on a variety of grounds - aesthetical, rhetorical, moral, logical, etc. - all of which are essentially normative.  No laws there, no necessity.  The same goes for the expressiveness of variable and function names used in program texts.  They have no intrinsic semantics; the programmer is free to construct any name that obeys the syntactic rules of name formation.  To the machine, whatever meaning they have derives entirely from the syntactic rules of the language.  If the names chose happen to look like natural language terms, they will (accidentally, as it were) convey some sense to the human reader.  But that sense has no necessary connection with what the program expresses formally.

Now obviously the goal is to construct names that have a clear meaning to the human reader _and_ that reflect the formal meaning of the program.  That seems to be a major part of the whole point of KLP: the coder "with thesaurus in hand, chooses the names of variables carefully and explains what each variable means."  But clearly we didn't need Knuth to tell us that variable names should be chosen carefully, so that hardly counts as a KLP innovation.  It's the "explains what each variable means" bit that has Knuth's attention; he wants that explanation to be expressed as a "literary" text in natural language, organized "in an order that is best for human understanding".  And in KLP that means a narratively structured order of explanation together with a print-oriented presentation of the result in essay form (using TeX, of course).

One question is whether this makes sense today.  When Knuth was writing in 1984 there was no Haskell, no Standard ML, etc.  LISP was around but apparently he didn't use it; presumably it was too much of a resource hog in those days (my guess).  In any case, the KLP tools he and his students came up with used languages like Pascal or C - imperative languages with assignment and lots of side effects.  It is hard to reason about programs written in such languages, and in _that_ case, detailed exegesis of the intended meaning of the code may be very helpful.

But those days are long gone.  Today our languages are vastly more expressive.  We have not only functional programming languages, we an emerging class of languages in which programs and proofs converge - languages like Coq, Agda, Idris, and others.  

[TODO: the gist of the argument, or at least this part of it, is that the holy grail is _not_ the ability to program in a natural language (which is the implicit ideal of KLP), even less program code integrated with lots of expository prose, but the construction of formal languages that are so expressive that we don't need anything else.  Compare mathematics: mathematical papers written by and for mathematicians are dense with formulae; the informal prose they contain plays only a supporting role, since the notation is expected to do the heavy lifting.  The ideal programming language would allow you to say everything you need to say in code (which would almost certainly make it a language for formal proof).  The implicit assumption here is that we're talking about expert use of the language, and texts written by and for experts.  Experts don't need explanations of the basics, something KLP afficianados tend to forget.]

# Misc points to be fleshed out

* Mastery - KLP seems to want code that is easily read and understood.  This would mean that any competent programmer could maintain a system just by reading the KLP "essays" that contain its code.  As opposed to needing to spend a lot of time studying the (raw, or traditionally documented) code in order to understand the system.  But if your job is to maintain or develop a complicated body of code, shouldn't you put in the time necessary to master it?  It might be a boring, pain in the neck task to read a bunch of poorly documented code, but people do it all the time.
* Constrast: KLP is all about elegant narrative prose.  Well, mostly about.  The rather stark contrast is with approaches that eschew narrative prose in favor of some kind of formal proof.  Take for example the introduction to The B Book: "This book is a very long discourse explaining how, in my opinion, the task of programming (in the small as well as in the large) can be accomplished _by returning to mathematics_."
* Pros and Cons.
* Distinction between API documentation and internals documentation.  And test documentation.
  * My preference is to keep code minimal - put the docs somewhere else, so they don't clutter my view of the code.  But maybe that only implies to internals documentation.  For the API and tests, mixing documentation and code makes more sense.  You're not explaining how things work, just what they mean, how they should be used.  Documentation of a function signature, for example, doesn't really clutter the code, since function sigs are short and concise.  Ditto for unit tests: the code of a unit test basically expresses and axiom or theorem, and is brief.  Added comments do not in general interfere with reading the code.  So a possible rule is: exegetical code (LP) for APIs and tests, minimalist code for implementation.
  
  ### CODE LIT
  
  # Some Literary Concepts Applied to Programming Texts

Refs:

* [Paratexts: Thresholds of Interpretation] (http://books.google.com/books/about/Paratexts.html?id=AmWhQzemk2EC) by Gerard Genette, Cambridge University Press 1997
* [Palimpsests: Literature in the Second Degree](http://books.google.com/books/about/Palimpsests.html?id=KbYzNp94C9oC), Gerard Genette, University of Nebraska Press, 1997
* _The Problem of Speech Genres_, in [Speech Genres and Other Late Essays](http://books.google.com/books/about/Speech_Genres_and_Other_Late_Essays.html?id=_LO_agE_GTcC), by Mikhail Bakhtin, University of Texas Press, 1986.  Bootleg copies can be found on the web.
* [On Philology](http://books.google.com/books?id=Z5LOraIe6pkC), ed. Jan Ziolkowski, Penn State Press, 1990
* [Future Philology?  The Fate of a Soft Science in a Hard World](http://www.jstor.org/stable/10.1086/599594)
* [Training Textual Critics in Textual Criticism](http://www.jstor.org/stable/20698017) Hans Gabler

## Varieties of Text

* Text
* Codetext
 * Code
 * Metacode, in languages like Clojure.  Metacode uses the same language as code (that is, the Clojure language) but functions as a kind of metadata or metacode.
* Datatext - the paradigmatic example is a file of numbers to be read into a program that crunches them, e.g. a CSV file containing data to be analyzed counts as a datatext.  But codetext is also datatext; to a parser, every codetext (program) looks like a datatext.  Datatext can be embedded in codetext.
* Paratext
* Metatext - distinct from metacode.  Text that is _about_ the codetext, e.g. explanatory documentation, is metatext in this sense.

## Purposes

Text may be address different audiences, for different purposes.  The requirements (norms) in each case may vary drastically.

* Pedagogical.  It is often assumed implicitly that pedagogical text involves lots of hand-holding and careful explicit guidance for the poor benighted reader.  But this not a requirement.  Case in point:  Smullyan's First Order Logic is a small pedagogical masterpiece that does almost no handholding.  Smullyan wastes no words explaining why things are the way they are, he just provides lots of definitions and examples that show that reader what things are (e.g. analytic tableaux and lots of other stuff), all in about 150 pages.  It is up to the student to do the work necessary to come to a genuine understanding of the material.  See also [Requiem for Philology](http://community.middlebury.edu/~harris/Classics/RequiemforPhilology.html), which makes a strong case for teaching the old-fashioned, where the teacher is a master who has something important to say, and not a nanny for students cannot or will not do the work themselves.

The relevance of this for LP is that the kind of detailed exegetical text usually recommended (Knuth's LP programs are paradigmatic) cannot be deemed the best way to do things, _even for teaching purposes_.  I think the example Knuth gives in his LP paper is a good example: I suspect that the raw code could be greatly improved, to the point that most if not all of his explanatory text could be eliminated.

* Scholarly communication.  The purpose is to communicate research to fellow professionals.  The needs here are quite distinct from the needs of pedagogical writing.

* Professional.  I.e. code written solely for the purpose of supporting some product or service for sale.  The ideal for this sort of code is that it would _never_ be read by anybody except a computer.  The need to read it only arises when bugs appear that need to be fixed or enhancements are required.  Even then, the commercial imperative dictates that the smallest possible amount of code be read; maintainers are virtually never expected to read all of the code of a largish system.  The programmers are expected to be professionals, so writing detailed pedagogically-oriented documentation would be a dereliction of duty in most cases.

The ideal here is engineering.  Bridge engineers do not (I assume) "document" their designs by explaining fundamental principles of engineering.  If they do need to include some kind of technical documentation they will do so by referring to the professional literature.  Software engineers should do likewise - if the code uses some specialized algorithm, it should not be documented directly in the code; rather, the code should contain a reference to literature whose purpose is explication of the algorithm.  That's not always possible, but even if there is no accessible literature, the algorithm should not be documented as part of an application.  Document the algorithm separately, in a document devoted solely to the explication of the algorithm.

## Palimpsest

A palimpsest is basically a text inscribed on paper from which a previous text has been erased or scraped off.  Back before the days of cheap paper this was not uncommon.

A program text under the control of a modern version control system can be viewed as a palimpsest.

## Transtextuality

One text making reference to or using another; the paradigmatic example is quotation.  So-called hyperlinks on the web implement a form of transtextuality.

## Hypertextuality

Today "hypertext" means, just about everywhere, HTTP-based links to other documents.  But that's really a misnomer; transtext would be more appropriate.  Genette takes the "hyper" in hypertext literally, and uses "hypertext" to refer to "superimposition of a later text on an earlier one that includes all forms of imitation, pastiche, and parody as well as less obvious superimpositions". (Paratexts, p. xix).  So a hypertext is superimposed on top of a hypotext (hyper=above, hypo=below).  Version control systems can be viewed as hyper-hypotext systems in this sense.

### PHILOLOGY AND HERMENEUTICS
### THE ART AND SCIENCE OF READING CODE
### ROLES AND REQUIREMENTS

# Roles and Requirements

Who are the consumers of code and documentation?  What do they want?

## Roles

* Programmers
  * Original developers of code
  * Clients who use code
  * Maintainers
  * etc.

## Requirements

### Programmers

### ON DOCUMENTATION


On Documentation

Two concepts of “documentation”

The text of the code, written in a programming language (not including comments).  This counts as documentation only insofar as it uses natural-language-like names for functions, ops, data, etc.  As code, such names have no intrinsic meaning; what meaning they have is strictly computational, determined by the purely syntactic rules of the programming language.  The code text expresses (specifies, determines, encodes, etc., but not describes) an algorithm.  But insofar as such names borrow from natural language, they also convey a sense or intensional meaning.  Unfortunately there is no way to ensure that the intensional (NL) and extensional (computational) meanings align.  It follows that the NL sense of the code cannot be fully trusted; in this it is like any documentation (you can call a factorial function “fibonacci”).
Natural language text about the code, and/or about the algorithm.  I.e. meta-code.  In general the task of this sort of documentation is to describe the code/algorithm, rather than express or specify it.  On the other hand, documentation might include a piece of text that expresses the algorithm, written in, say, a formal specification language.

[NB: does code describe algorithm?  That doesn’t sound right; in some sense the code “is” the algorithm.  But that doesn’t sound quite right either.  Maybe the best way to put it is that the code encodes the algorithm (hence “code”).  But what is the precise nature of this concept of “encoding”?  Isn’t it just circular to say that code encodes algorithm?  Better yet:  code expresses algorithm.]

Expressivity:  code expresses algorithms: what exactly does this mean?  What is the precise nature of the relation between code and algorithm?  This takes us into deep philosophical waters - e.g. what is an algorithm, anyway?  Do algorithms have a form?  What’s the difference between an algorithm and a process?  Etc.

Laws v. Norms

The expression of an algorithm in code involves a relation of necessity: the algorithm you get when you run the code is necessarily the “same” as what the code expresses.  The algorithm cannot deviate from the (meaning of the) code text.

By contrast, NL meta-documentation answers to the code as a norm.  The meanings expressed by the NL documentation can (and usually do, alas) deviate from the meaning of the code text.

In other words, from the machine perspective, code expresses a law.  From the documentation perspective, code expresses a norm.


Learning

How can we discover or learn the meaning of a piece of code?  There are two sources of “evidence” as to the meaning of a program:  a) the code itself; and b) the behavior of the code, as manifested in a trace from running it.

So one way to support easy discoverability would be to support a “minimal semantic demonstration” (MSD) of the code.  This would amount to a specialized variety of unit test.  Invoking MSD on a function would result in a display of the form “input -> output” which would demonstrate the semantics in action.  For example:

    (msd ‘factorial)
    -- MSD:  factorial
        (factorial 0) -> 1
        (factorial 1) -> 1
        (factorial 2) -> 2
        (factorial 3) -> 6
        (factorial 4) -> 24

Implementing this as a kind of unit test would serve both as a minimal QA device and as a discovery device.

### TESTS AS DOCUMENTATION

One way to support easy discoverability would be to support a “minimal semantic demonstration” (MSD) of the code.  This would amount to a specialized variety of unit test.  Invoking MSD on a function would result in a display of the form “application -> output” which would demonstrate the semantics in action.  For example:

    (msd ‘factorial)
    -- MSD:  factorial
        (factorial 0) -> 1
        (factorial 1) -> 1
        (factorial 2) -> 2
        (factorial 3) -> 6
        (factorial 4) -> 24

Implementing this as a kind of unit test would serve both as a minimal QA device and as a discovery device.

### RESOURCES

# Resources

## Papers

[How Programmers Comment When They Think Nobody's Watching](http://www.cgl.uwaterloo.ca/~commenting) " Documentation is essential to software development. Experienced programmers know this well from having worked with poorly documented code. They wish to improve their documentation techniques and habits, but there is little consensus for them to follow. Somehow, the many different standards must be compared objectively. This desire motivates my work, which aims to better understand existing documentation practices. ... This work focuses exclusively on comments within the program code."

## Blogs

[The Low Quality of Scientific Code](http://techblog.bozho.net/?p=1423)

## Tools

* [Concordion](http://concordion.org/) "Concordion is an open source tool for writing
automated acceptance tests in Java (or .NET, Python, Scala, and Ruby)...Concordion acceptance tests are so readable they can double up as system documentation."
* [Cucumber](http://cukes.info/)

## Portals

* [literateprogramming.com](http://www.literateprogramming.com/)

## Mailing list threads

* [Proposing a new Clojure documentation system (in Clojure)](https://groups.google.com/forum/?hl=en#!searchin/clojure/Proposing/clojure/oh_bWL9_jI0/z9qN-MzL_5IJ)
* [deep thinking](https://groups.google.com/forum/?hl=en#!topic/clojure/YOeQVUWhUtA)
