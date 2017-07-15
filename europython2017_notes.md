# Europython 2017

## Day 0 - Sunday (beginner workshops)


## Day 1 - Monday (conference)

### Keynote
* Python community celebrates compatibility
* Python needs internal updates that will break compatibility (Python 4?)
* On the way to improve packaging system
* C-extensions: use cffi if possible (not with numpy objects) if you want to distribute

### Testing in Layers
* www.aleax.it/europy17.pdf
* Old: white-box, black-box testing
* Today: unit-tests, integration-tests, sometimes human QA
* Humans are bad testers
* Layers: unit-tests (fast), higher-layer tests (match code layers), full integration tests
* CI unit-tests with each ‘save’ operation (NO context switching)
* Ensure reproducibility (set seeds, fake time, …), test driven approach to fixing bugs
* Test: remove dependencies if 100% understood, otherwise do 2nd layer test: emulate
* Reuse tests in all layers
* Mid-layer: mock dependencies or use actual dependencies if fast enough (measure)
* High-level: mock mid-layers or use actual mid-layers, with actual: mock or fake lower level
* mock: fast, least accurate, actual: least work, make sure it's fast, fake: great, but a lot of work to create
* intended changes: let existing tests fail before changing them
* fast-unit tests might miss something: log everything, regularly check logs for other problems
* Move to widely used libraries and assume they are correct: faster or fewer tests

### Kubernetes
* Make infrastructure homogeneous (virtual & bare metal)
* Separate App Ops from Infra Ops
* Easy scaling, easy updates, smooth processes
* Load balancing, secret management, batch execution
* Backbone: etcd distributed database (copies)
* Centralized: API server on Master node, handles all communication
* Node-internal network handling (kubernetes proxy)
* Number of Pods (smallest deployable) in a Node
* Declarative (set how state should look like), "Deployments"
* Explicitly expose using “service”

### TCP/IP animated
* Interactive explanation of the protocol

### Measure don’t guess
* Interactive code, see file
* There are also line-by-line profilers

### REST frameworks review
* Which tool to choose?
  * The ones used recently (already known)
  * Which framework best fits needs? (feature overview, examples)
* Frameworks
  * Django rest framework
    * obvious choice for Django
  * Flask restful
    * parser similar to argparse
    * obvious choice for Flask
    * Rebuild existing Flask to use Flask restful!
  * Falcon
    * single use case: HTTP APIs
    * reliable, high-performance for this task
    * microservices
  * Eve
    * Human readable, etc.
  * Tastypie
  * API Star

### Effortless Logging
* Documentation - information for developers while coding
* Logging - information for developers while running
* Logging module: Loggers, handlers, formatters, filters
* logging.getLogger instance
* Option to propagate records to parent handler
* Enable / disable loggers, categorize loggers
* exc_info=True full stacktrace

### Mock it right
* Find all the points that can go wrong, write test for each
* External dependencies need to be replaced
* unittest.mock.Mock - very basic fake objects
* spec_set: make sure production actually (still) has the tested part of the mocked object
* spec: similar but not as powerful for full objects
* cannot pass mock object: use patch
* unittest.mock.patch
* mocks and patches have reversed order

### Lightning talks

#### chatops is coming to foss
* coala/corobo
* chatbot for newcomers in git project (can't give all access rights immediately)
* assign yourself to issues etc.
* slack, telegram, gitter

#### pycon.de 25.-27.10.

#### Ipynb_output_filter
* ipython notebooks in git

#### offtopic & community
* no skills, make friends & have fun -> offtopic channel
* more interactions, related to interests, more fun
* community can engage without having to do work

#### firefly - deploying functions made easy
* expose function as web API
* rorodata/firefly

#### Edgy.project
* python project artifacts manager
* all the important files created from one small config file
* no additional dependency

#### beyond coverage
* test coverage is just a reference
* necessary, not sufficient
* maybe some code is missing
* good software: tests >> source
* thoughtful testing!

#### Source-lift.com
* Kiwi.com
* flight-cost aid
* apply if you want to create an event and are a popular foss
* ethereum & smart contracts

#### sanest
* wbolster/sanest
* sane nested dictionaries and lists
* nested operations
* type checking
* currently json only
* type safe & fail fast
* multi index, slice syntax
* wrapper, no copies created
* meaningful errors


## Day 2 - Tuesday (conference)

### Keynote - Data visualization
* Company Tulpinteractive @JanWillemTulp
* named list in twitter, name extraction
* rotterdam architecture state archive
* made accessible online, search bar
* common practice, assumes you know what you're looking for
* show structure, patterns, outlier
* visual design & interaction, concept, data
* what does the archive look like?
  * What does the content look like?
  * What does the structure look like?
* Title, metadata, folders & files with labels
* natural language processing, person & location identification
  * Frog (NLP for Dutch), alternative to NLTK
* Clustering based on content, sized dots
* lists left & right: beginning of words, end of words
* 3D tree of archives, clustered
  * select based on number of nodes (linechart)
* what makes it interesting
  * people differ, time can change interest
* new vs common, comprehensible vs incomprehensible
* What's in a star catalog
  * ESA star mapper
* storytelling with data
  * martini glas - narrow first, widen later
  * guide user step by step
* trees in the world, nature
  * sattelite images
  * actual counting by people in various locations, for density
  * latitude, longitude, tree density (square kilometer)
  * solid globe, colored bars
* characteristics of the data, reused in the visualization, metaphor
  * trees / green, tall, bumpy
  * deaths / blood
  * wind / flows
* Dutch national elections
  * won, lost,  coalitions, own city
  * which cities vote similarly
    * click on town, show similarness by dot size & color
    * alternative: city size
    * regional clusters
* "Hook model", Hooked - How to build habit forming products
  * trigger, action, variable reward, effort
* D3 framework, 3 JS, custom
* web based frameworks, data prep with python, tableau

### PostgreSQL & Python
* Open source, community, documentation
* stable, feature rich, frequent releases
* feature overview
* geospatial extensions
* python and postgreSQL benefit each other while jointly being used in projects
* library: psycopg2 (and many others)
* python INSIDE PostgreSQL PL/Python
  * take action on insert, update, etc.
* check out: multicorn
* github.com/gcalacoci
* backups: Wal-E, barman
* check out: Patroni (high availability)
* pgcli less powerful but smart cli
* POWA workload analyzer
* pgAdmin4

### Facebook: Datacenters at scale
* automate basically everything, because scale demands it
* facebook does hackathons to solve issues (prototypes)
* python helps create fast prototypes
* python also good for production
* Apache thrift
* facebook/sparts services framework for python
* facebook builds binaries
* one build system: buck (open source)
  * ships all dependencies
  * meta stats availabe
* bittorrent: distribution of binaries to servers
* robots are coming !@! - and they'll need your cloths

### SAP: Test database HANA with python
* SQL interface
  * SQLAchemy, Django can provide interfaces
* unit/component tests in C++
* integration and end-to-end tests in Python
* Gerrit code review system
* Review AFTER tests, lints etc.
* Jenkins CI
* All tests are saved into a database (with web UI) for historic reviews
* Huge testing setup
* Divide and conquer
  * Pull & build is stored for later use
  * Setup & long test divided in multiple parallel setup & test parts
* tests are re-run to check for technical issues leading to fails
* test scheduling
  * configuration: which tests to run to get the most benefit, layers
    * based on branches
  * observe and react: re-schedule failed tests, automated review
* Waiter collects information from multiple sources, coordinates with Jenkins
* First in first out -> Prioritized test queue
* large installer, test data between small and large -> local caches
  * 66% traffic reduction
* healthy test environment
  * external dependencies
  * parallel testing
  * health checks before and while testing
* Non-developers can write tests

### Writing beautiful code
* rorodata
* programs must be written for people to read
* choose meaningful names
  * avoid generic names
  * avoid abbreviations
  * avoid data types as names
  * nouns: variables & classes
  * verbs: functions
  * use plural for a list / array / vector
  * i,j only loop indices
* Program organization
  * Divide & Conquer
  * The number of objects an average human can hold in working memory is 5-9
  * avoid duplication
  * avoid deep nesting
  * handle errors separately (don't hide main functionality)
  * suppress implementation details (use functions for that)
* @anandology

### Improve your developer's toolset
* tmux
  * session names, window names
* tmuxinator
  * save sessions: layout etc.
* zsh & oh-my-zsh (prepared configuration)
  * easy & smart path changing on many levels
  * many plugins
* fish
* dotfiles

### Lightning talks

#### Found a security issue
* vulnerabilities everywhere
* make it easy to contact you, take reports seriously
* document fixed issues
* don't hide issues

#### Vacation diary
* Don't only take pictures, experience the moment, make memories

#### Newcomers perspective to FOSS
* Contribute as a learning experience (coala)
* Have something for beginners to work on

#### iGitt
* in gitmate.io, comments and labels added to github
* interface for adding those comments on different platforms
  * github, gitlab, ...

#### Speed packaging
* flit
* Wizard asks for missing information, creates necessary files
* add readme file
* flit publishes it to PyPI

#### Research Software Engineer
* new name for people bridging between researchers in academia and software developers
* movement got some steam! (money, conferences, ...)

#### python version confusion
* "python" usually starts python2
* archlinux changed it to python3 and fixed the regressions
* pep394 fixes it to python2 (ubuntu, fedora)
* also used in many package names
* explicit is better than implicit
  * use python2 or python3 explicitly

#### python in architecture
* building information model
* database of 3d elements (autodesk revit)
* .NET API -> revitpythonshell, pyRevit

#### PyConPl'17
* snake tournament
* python riddles
* python-challenges.com

#### Stuff
* dothub, github configured by a yaml file
* sealed mock, no automatic extension of the mock

#### Fearless testing async HTTP requests (aiohttp)
* how to test http requests?
* found no solution for mocking it

#### PostgreSQL needs you

#### Ace your technical interview
* show proof that's related to future project
* show you've done the hard parts
* positive attitude
* live coding: solve problems, can code, know edge cases
* find out structure beforehand and prepare
* ask questions about what might be relevant
* communicate technical concepts well


## Day 3 - Wednesday (conference)

### Keynote - if Ethics is not None
* Data scientist
* talk about ethics in work place - seldom, should more?
* Ad: SAGE tracking all aircaft over the US, shooting incoming enemies
* Norbert Weiner: Cybernetics, Computer = slave labour
* we're working of automating jobs away - humans competing with slaves
* Joseph Weizenbaum, ELIZA, automation in banking
  * alternative: social invention instead of technical?
  * regionalization?
* technology vs. social progress?
* consolidating existing power distribution?
* participatory design
* psychology: compromise changed to desired solution
  * be honest about compromises!
* tools to support our ethics, politics instead of working against it?
* computer literacy - have it be as common as reading/writing
  * instead of building elites
* rare knowledge: elite? power? responsibility?
* Computer Professionals for Social Responsibility
* Who is responsible
  * Creator? User? User informed enough?
* AI is NOT a human being, it's more like a reference book
* good models, need less data about individuals
  * data hygene not enough even if everyone would do
  * data needs to be regulated
  * EU law is a good step, but not global and not yet interpreted
* How do we hold each other accountable
  * share our stories
* Using technology to improve society, something started in this generation?
* Progress will continue - how can we take social responsibility serious?
  * Conferences, more discussions, being open

### README
* open source survey - open data project
* documentation is highly valued, but often overlooked
* licenses are most important one
* documentation leads to inclusive communities
* many people need simple english
* Readme is the first impression of your project
* First contact point in case of problems
  * Be understanding and straight to the point
* there's no standard, examples
  * audreyr/cookiecutter
  * pallets/flask
  * django/django
  * pypa/pip
* Readme consumption via github html or simple text
* expectation of the users to find information in known places
* ask others for contribution to readme
* docs or it didn't happen
* Empathy for users
* Tell a story
* Set expectations
* What does the project NOT do
  * Link related projects
* State maturity
* Prerequisites: OS, Python version, dependencies
* preferred installation method
* List most important features
* Give examples
* FAQ in normal documentation (not readme)
* link to issue tracker
* communication methods
* who is behind the projetc
* how can people contribute, how can they become a core team member?
* contributor code of conduct
  * guideline of how to interact with the community, which punishments
* NOT in the readme
  * just read the code
  * easy, obvious, just
* Improve your projects
  * encourage documentation commits
  * beginner guide to docs, writethedocs.org, has conferences
  * repo tells a story

### bonobo - simple ETL
* extract transform load
* simple stream, today additional steps like logging
* many tools with graphical interfaces
* alternatives: Bubbles, PETL, others
* related: Joblib, Dask, Pandas, Toolz
* IFTTT, zapier
* spark, hadoop, google big query, amazon EMR
* Story: Data integration with one partner well in old tools
  * copy pasted for other partners, bad
* define three functions (extract, transform, load)
* create a graph for running them in order
* example: multi-line entries with different content into dicts with proper keys
* transformations can be: functions, generators, iterators, classes, configurable classes, runtime injection
* various connections to other tools
* works with url requests, pagination
* selenium, controls browser for easy web-scraping
* target: 1.0 early 2018
* data processing for humans
* errors: unrecoverable stopping the graph, handle recoverable line errors
* similar to kafka

### evolve code
* studycode.org
* automate work, even higher skilled ones
* IBM Watson
  * all kinds of assistants: doctor diagnostics, teachers, ...
* genetic algorithms
  * random strings, fitness function, changes, goal reached?
* programs are more complicated, random code is usually invalid
* turing machine is a simple (but full) version
* primaryobjects.com
* brainfuck language
  * 8 characters, basically a turing machine
* evolving in this language
  * add timeouts
  * several updates to fitness function, selection process, mutation
* emmagordon/genetic-algorithm
* maybe evolve program structure instead of text representation

### pandas indexes
* series, default increasing numbers
* series[0], series[3:6], series.iloc[3:6]
* series.index = ...
* still can use numbers, additionally series['D':'F']
* pd.concat preserves labels
* unique indices necessary for using above slicing with index labels
* multiple dimensions
* index, multiindex, datetime, timedelta, ...
* dataframe, multiple series with the same index
* don't need panel 3D any more, can do everything with multiindices
* df[2] column
* df[2:4] rows
* df.iloc[2:4, 2:4] segment
* df.iloc[:, 2:4] columns
* axis 1 horizontal (top-bottom), axis 0 vertical (left-right)
* label index: df.index = ...
* label columns: df.columns = ...
* df['C05'] colummns, df['R02':'R05'] rows, as above
* df['C10'] = new_df add new column - index in respected
  * NaN if missing in new column, not added if missing in df
* pandas creates copies when necessary
* df.join(df2, how = '...')
* df.drop to remove data
* df.groupby and summarizing function creates a multiindex in resulting df
* look at df.index, df.index.levels, df.index.names, df.index.values
* df.index.get_level_values()
* df.loc() access by multilevel index, can use first few levels
* datetimeindex
  * df.index = pd.to_datetime(df['timestam'])
  * proper representation of date & time in plots and functions
  * df.index.date, df.index.week, df.index.weekday, df.index.hour
  * df['2014-09']
  * df['2014-09-01':2014-09-20']
  * df.index.hour > 12
  * df.resample('D') + aggregation function (or multiple with agg())
  * cheat sheet

### sustainable software, research
* software sustainability institute
* poor availabiliy of scientific software, if availab often badly documented
* will the code work in 5/10/20 years? can it be found? can it be run?
  * otherwise recreate the wheel every time
* scientific software
  * investigate complex, unknown phenomena
  * developed over long time, lots of collaboration
  * scientists write that, not software engineers
* scientific method doesn't stop at using computers as a tool
* version control
  * log + aids collaboration
* testing (need to be sure it works, understand limitations)
  * unit tests, integration tests
  * regression tests (different versions of the code, should not get worse)
    * added backward compatibility
* controls - simple input data with known solution
* isolate random parts, test averages, check limits, conservation of physical quantities
* convergence tests (does improve with better algorithms?)
  * numpy.isclose, numpy.allclose
* TraviCS, CircleCI
* github harpolea/
* codecov.io
  * shows non-tested edge cases
* documentation
  * sphinx, host at Read the Docs
  * examples
  * Reasoning and example code in one file (jupyter notebook, etc.)
* make findable: opensource, DOI, zenodo
* reproducible runtime environment
* www.software.ac.uk
* spread?!?
  * awareness, pressure on journals
* overhead
  * actually saves time by catching problems early, even within one piece of work
* need something better than github (DOI)
* there are websites for scientists to dump data

### A gentle introduction to data science
* Marc Garcia, datapythonista, Badoo, NumFOCUS
* brain architecture

### Better Stream processing with python
* Winton, Andreas Heider, Robert Wall
* binning to proper / valuable sizes
* event streams, event bus
* apache kafka, message broker
  * topics, partitions, message ordering
* Flink, beam, storm, nifi, samza, spark
  * nothing really fit
  * heavy weight & JVM, python 2nd class citizen
* Kafka Streams
  * simple library, not framework
  * event by event
  * stateful processing, joins, aggregations
  * distributed, fault tolerance
  * Java only
* kafka-python (pure python)
* confluent-kafka-python (wrapper for c library)
* homegrown script: all the features and reliability is missing
* wintoncode/winton-kafka-streams
* start with zookeeper

### Lightning talks

#### Build your own twitter bot
* birdy
* LuRsT/mylittlebotie

#### gilectomy update
* memory issues, function calls, frame objects
* reference management, long delay before stuff is freed

#### google summer code experience
* couldn't enter, test results bad
* blame - first check on yourself
* some help from colleague, entered
* get help, focus, get shit done

#### massage training
* in tradition of rob collins, rip
* also the PySF needs money

#### sphinx gallery
* help teaching your software
* how I would do ...? - stackoverflow
* inspired by matplotlib gallery (all the examples)
* use sphinx gallery to make gallery for your project

#### when is a memory leak not a memory leak
* still got references to objects (maybe in some library you're using)?
* interpreter doesn't return your freed memory (python 2.x, see stackoverflow)
* 100% CPU? In the Twisted TCP server send buffer

#### anyone can dig a hole but it takes a real man to call it home
* imposter syndrome, perfectionist, not good enough, only success matters
* what do you value in life?
* change perspective to be happy

#### something
* energizer
* micro-wave (crowd)
* increase self-confidence
* learn something about yourself
* great tool to push people to get out of comfort zone
* make people fascinated
* coala

#### slicing a carrot
* Plone, new UI in development
* sushi chef needs 15 years to properly slice a carrot
* UI - mobile first (users in bangladesh that only will ever have a phone)
* reusable components

#### datetime.astimezone confuses me
* can now be called on naive instances
* presumes naive have local timezone

#### tox
* automate testing, build docs etc.
* companies take FOSS for granted, expect stuff to be fixed quickly for free
* change attitude from the ground up, have free time to support used projects

#### one keyboard to rule them all
* compose key for multi language support

#### async.io
* awaitables

#### PyCon UK
* BrExit =/

#### python-goto
* snoack/python-goto

#### Django + SQLAchemy
* Django is slow to compile SQL
* Don't switch to plain SQL, but use SQLAchemy


## Day 4 - Thursday (conference)

### Keynote - Different roads we take
* learning python, programming is not linear
* some people are not software developers (profession)
* people learn differently / have different things that they are talented in
  * graphical people, theoretical people
* title: don't artificially narrow it down, make it as wide as it is
* Django: abstraction layers make technology accessible to more people
* frameworks are great!
* handholding really helps!
* empbrace diversity in skill sets
* need those skill sets in projects!

### Maschine learning as a service
* repo: https://github.com/amitkaps/full-stack-data-science


## Day 5 - Friday (conference)

### Keynote - Python & Africa
* PyCons in Africa
* Python Workshops in Africa (Django girls)
* Non-existent community before
* Spend time with people, transfer of ideas, understand each other
* Be bold! Conference was a success, great adoption
* Sparked attendees to teach python at schools
* Now taught in universities and schools
* Don't need a community to begin with, create the community AT the conference
* coaching for mentors to work with traumatized girls
* teaching computers from scratch, giving out raspberry pis
  * taking fears, givig confidence
* Africa huge continent, vast ethnic and cultural diversity
* currently software is mostly bought, need to build it by themselves
* hobbyism, when free is unaffordable
  * needs spare money, spare time - no time for hobbies in Africa
  * everything needs to be profitable - work, not fun
* Snakes in Africa are NOT funny, "Python" very negative, demonic
* African time: 3 hours buffer; personal conversations
* little confidence of Africans in African technoloy, needs change
* come to an african PyCon, be a Pythonista

### Training - Testing data
* Data Validation in the Wild
  * is hard
* data errors are costly
  * https://www.researchgate.net/publication/304054978_Towards_reliable_interactive_data_cleaning_a_user_survey_and_recommendations
  * https://www.ocf.berkeley.edu/~sanjayk/wp-content/uploads/2016/06/18.pdf
* repo: https://github.com/kjam/data-cleaning-101
* quality evaluation: valid, accurate, complete, consistent, uniform, repeatable
* reliability: correlation, temporal stability, internal consistency
  * (more new users -> more activity) (same traffic patterns) (more clicks = more page views)
  * finding good tests is very difficult (collaborate!)
* validity: predictive validity, measurement or metric validity, trends or noise
  * (testing past models, predictions)
  * (what does it measure, how, is it valid) (fallacies of metrics)
  * (tracking patterns & outliers) (understanding biases) (handling non-signals)
  * be super annoying to yourself, track and log, check non-engagement
* statistical models & measurements
  * make good use of distributions if one fits the data!
* outliers, anomalies, extreme values
  * do normal outlier detection work?
  * can you easily predict normal values (including preprocessing etc)
  * do you throw out anomalies? how many? how come?
  * do you analyze occurrence of anomalies or extreme values?
* anomalies don't always need investigation - sometimes checking for reoccurrence is enough
* margin of error
  * how relevant are accuracy, error and confidence measurements
  * what's the margin of error you need to meet?
  * do you have the ability to test new ideas, models, etc.
* valid values / types
  * alecthomas/voluptuous
  * guyskk/validr
* don't use csv if you need performance
  * databases
  * https://parquet.apache.org/
* assert can be disabled by a python flag
* uses dask or numpy instead of pandas
* many projects uses hypothesis to find edge cases
  * collect the failing tests
* more libraries
  * marshmallow
  * apache avro
  * scikit-learn cross-validation
  * test ml features: machinalis/featureforge
  * built-in stats: "statistics" in python
* data unit tests
  * not writing tests
    * prototyping?
    * exploratory work?
* test small unilt of code; define in, out, behavior (no integration)
  * nasty mindset, CRUSH the code
* data science uses code!
* test small units of data
  * (within expected ranges) (display expected heuristics) (show anomalies, erratic behavior)
* libraries
  * unittest.mock
  * faker
  * pereoraga/csvfaker
  * Ned Batchelder's testing talk
* version control, automated testing
  * pytest, CI (Jenkins, Travis, TeamCity, ...)
* www.bettercode.reviews
* existing toolset sometimes have it built-in (apache spark, apache beam)
* tests, incoming
  * thresholds, distributions, correlations
  * anomalies & outliers - how handled
  * automated fixing
* selling it to company
  * saves money, part of core decisions or product, risk reduction
  * lost revenue, hours lost chasing bugs etc.
  * poor & costly decisions
  * inaccurate predictions
  * gained
    * happier employees, easier hires
    * ability to automate and TRUST more workflows
* Academia, papers, more research, reproducible science
  * much Java
  * Katara: Crowd + information extraction
    * knowledge base, graph databases (different nodes + different relations)
    * constraint inference
    * crowd validation
      * evolve constraints
    * databugger, (now rdf unit)
      * test driven development in data science
      * schema patterns & unit-test
      * also knowledge base
      * errors in wikipedia found using constraints
    * "unsupervised" anomaly detection
      * small dataset -> generative network
        * oversample use case if small
      * deep learning problem
* treat data piplines as production level
* blog.kjamistan.com
* @kjam, katharine@kjmistan.com

### Tensorflow
* open source, deep learning, version 1.0.0 since 2017 feb
* input -> model -> output
* cost function: difference between output and expected output (labeled data)
* optimizer changes model based on cost
* error: sum([y - model(x)]**2)
* error -> follow the steep of the function to the minimum
* cat [0, 1], non-cat [1, 0]; output [0.15, 0.85] probabilities
* first layer extracts more basic information, 2nd layer classifies
* alesolano/mastering_tenorflow
* ML better with little data, deep learning is good with tons of data
* Keras: simplified interface for Tensorflow

### Microservices & containerization
* architecture style: small services, lightweight communication
* specialization of service oriented architecture (small difference in implementation)
* minimal, independently deployable, configureable, replaceable,
* organized around business capabilities, smart endpoints, elasticity,
* resilience, versioning, infrastructure automation,
* centralized logging and monitoring, encapsulation, stateless
* APIs as communication, decentralized: no single point of failure,
* right tool for the right job, polyglot persistence, single responsibility,
* scalability, decoupled, bounded context,
* end-to-ond ownership and independent governance
* pip install nameko
  * get, post, RPC over AMQP, PUB-SUB, WEB SOCKET
  * unit-testing service
* traditional (monolithic) / virtualization (vm) / containerization (docker)
* git, jenkins (creates image), docker run tests, publish image
* when to use microservices
* common mistakes
  * shared database
  * own service discovery (use existing!)
  * forcing to use microservices
  * logging & monitoring as afterthough (do it right away)
  * one technology / framework everywhere (best tool for the job!)
* trade offs
  * operational and tools cost
  * cultural cost
  * distributed systems complexity
  * well defined interfaces and documentation is a must
  * devops first architectural style
  * team communication overhead

### overcoming cognitive bias
* our brains: use heuristics, automating pattern-matching, fill in the blanks
* sometimes it's faulty
  * patterns that don't exist, correlation != causation, etc.
* conferences, often few women in tech -> patterns
* #ILookLikeAnEngineer
* bias blind spot (on ourselves)
* intelligence uncorrelated with bias awareness
* confirmation bias, ingroup bias, projection bias, selective perception,
* status quo bias
* we test for edge cases! we try to disprove
* blind auditions: hiring by skill without any clue for race or gender
  * equal rates!
* it's how our brains work
  * awareness & conscious effort
  * welcome and mentor new pythonistas
  * encourage people to go to and speak on conferences
* hiring: textio.com removes gender from job ads
* remove name, universities, etc. from resumees
* gapjumpers.com
* culture fit? ingroup bias!
* first look for strengths, reasons for hiring
  * look for imposter syndrome
* close wage gaps (same level and work) from your side
* undoing the mental model: meet more people that don't fit the stereotype
* youtube talk: diversity as a dependency
* look at despicable maschines talk: AI / ML & biased training data

### Lightning talks

#### Can we talk to jupyter
* bit.ly/talk-to-jupyter
* arguments for jupyter notebooks
* stackoverflow workaround, only for notebooks not dashboards
* Jupyter.notebook.kernel.comm_manager.register_target ...
* query parameters in the browser URL can be accessed

#### Massaging for the PySF
* 1000 raised
* pyweek.org/24
* games!

#### Malta <3 Python
* setting up Python user group: PyMalta

#### run python with warning ENABLED
* very much repeatedly, tons of examples
* python3 -Wd -b
* python2 -Wd -t -3

#### Threading in python
* GiL has been removed
* need to think about multithreading
* tools, c-extensions
* need to raise money

#### Awesome talks
* give talks often
* get them evaluated!
* structure beats slides
* story beats CV
* take-away value beats completeness
* google github speech_projects

#### tdd reality check
* (test driven development)
* testing is big / known, no more tdd talks
* think about projetc, define tests first, develop

#### EuroSciPy
* two days of tutorials (beginners and advanced track)
* two days of main talks
* sprints
* keynote: how to fix scientific culture

#### culture -> perception of music
* audacity, scales
* tinyurl.com/PerceptionMusic

#### ssim
* Flight data, format, .SIR files
* Schiphol-Hub/ssim

#### Pyjok.es
* help get jokes!
* pip install pyjokes

#### Introduction to mocking
* hacksoft.io
* Fast, isolated ,repeatable, self-validating, timely/thorough
* dependency on other functions: mocking / patching

#### PyConWeb

#### PythonBrasil

#### How to get your pants stolen

### Closing session
* sprints in wiki
* sponsor europython!
* volunteer team on the website
* need more for next year!
* EuroPython Society


## Day 6 - Saturday (sprints)

## Day 7 - Sunday (sprints)
