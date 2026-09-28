# Academic Foundations

## Contents
- 1. Problem → abstraction → encoding/interaction → algorithm
- 2. Why / How / What task abstraction
- 3. Overview → zoom/filter → details; relate/history/extract
- 4. Interaction by user intent
- 5. Fluent iterative visual analysis
- 6. Coordinated Multiple Views
- 7. Perceptual effectiveness of graphical encodings
- 8. Visualization grammar & interaction grammar
- 9. Analytic provenance
- 10. Problem-driven design study method
- 11. Evaluation scenarios
- 12. Scalable linked views
- How to cite the engineering pattern


This reference maps the skill's engineering rules to established visualization and HCI literature. The skill itself is a synthesis; the name “Research Visual Analytics Panel Design Pattern” is not a standardized academic theory.

## 1. Problem → abstraction → encoding/interaction → algorithm

**Tamara Munzner (2009), “A Nested Model for Visualization Design and Validation,” IEEE TVCG 15(6):921–928. DOI: 10.1109/TVCG.2009.111.**

Key contribution: a four-level model—domain problem characterization, data/task abstraction, visual encoding & interaction, and algorithm design. Errors upstream propagate downstream.

**Skill implication:** never begin with a chart library or layout. Establish the domain problem and abstract tasks first.

## 2. Why / How / What task abstraction

**Matthew Brehmer & Tamara Munzner (2013), “A Multi-Level Typology of Abstract Visualization Tasks,” IEEE TVCG 19(12):2376–2385. DOI: 10.1109/TVCG.2013.124.**

Key contribution: separate why a user acts, how the task is performed, and what data/input-output is involved; complex tasks can be sequences of simpler tasks.

**Skill implication:** write analysis questions and task sequences before view design.

## 3. Overview → zoom/filter → details; relate/history/extract

**Ben Shneiderman (1996), “The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations,” IEEE Symposium on Visual Languages. DOI: 10.1109/VL.1996.545307.**

Key contribution: the visual information-seeking mantra and a task taxonomy including overview, zoom, filter, details-on-demand, relate, history, and extract.

**Skill implication:** support progressive exploration and avoid dumping all detail into the first view.

## 4. Interaction by user intent

**Ji Soo Yi, Youn-ah Kang, John Stasko, Julie Jacko (2007), “Toward a Deeper Understanding of the Role of Interaction in Information Visualization,” IEEE TVCG 13(6):1224–1231. DOI: 10.1109/TVCG.2007.70515.**

Seven interaction categories: Select, Explore, Reconfigure, Encode, Abstract/Elaborate, Filter, Connect.

**Skill implication:** describe interaction by what it lets the analyst do, not by low-level widgets.

## 5. Fluent iterative visual analysis

**Jeffrey Heer & Ben Shneiderman (2012), “Interactive Dynamics for Visual Analysis,” Communications of the ACM 55(4):45–54. DOI: 10.1145/2133806.2133821.**

Key contribution: visual analysis is iterative view creation, exploration, and refinement; tools should keep interaction close to the pace of thought.

**Skill implication:** reduce hidden state and interaction friction; favor continuous analytical flow.

## 6. Coordinated Multiple Views

**Jonathan C. Roberts (2007), “State of the Art: Coordinated & Multiple Views in Exploratory Visualization,” CMV 2007. DOI: 10.1109/CMV.2007.20.**

Key contribution: coordinated multiple views are a mature approach for exploratory visualization, where views complement one another and share interaction state.

**Skill implication:** multi-panel layouts should coordinate selections, filters, or focus—not simply coexist.

## 7. Perceptual effectiveness of graphical encodings

**William S. Cleveland & Robert McGill (1984), “Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods,” JASA 79(387):531–554.**

**Jock Mackinlay (1986), “Automating the Design of Graphical Presentations of Relational Information,” ACM TOG 5(2):110–141. DOI: 10.1145/22949.22950.**

Key contribution: visual encodings differ in perceptual effectiveness; design can be reasoned about in terms of expressive and effective graphical languages.

**Skill implication:** choose channels for analytical accuracy and semantics, not decoration.

## 8. Visualization grammar & interaction grammar

**Arvind Satyanarayan, Dominik Moritz, Kanit Wongsuphasawat, Jeffrey Heer (2017), “Vega-Lite: A Grammar of Interactive Graphics,” IEEE TVCG 23(1):341–350. DOI: 10.1109/TVCG.2016.2599030.**

Key contribution: layered/multi-view composition plus a declarative grammar of interaction based on selections.

**Skill implication:** treat selections and linked state as first-class semantic objects rather than scattered UI callbacks.

## 9. Analytic provenance

**Eric D. Ragan, Alex Endert, Jibonananda Sanyal, Jian Chen (2016), “Characterizing Provenance in Visualization and Data Analysis,” IEEE TVCG 22(1):31–40. DOI: 10.1109/TVCG.2015.2467551.**

Key contribution: organizes types and purposes of provenance records in visual analytics.

**Skill implication:** record history when the route to an insight matters; provenance can support recall, reproducibility, communication, and evaluation.

## 10. Problem-driven design study method

**Michael Sedlmair, Miriah Meyer, Tamara Munzner (2012), “Design Study Methodology: Reflections from the Trenches and the Stacks,” IEEE TVCG 18(12):2431–2440. DOI: 10.1109/TVCG.2012.213.**

Nine stages: learn, winnow, cast, discover, design, implement, deploy, reflect, write.

**Skill implication:** for serious domain projects, validate the real problem and collaborators before over-investing in visualization novelty.

## 11. Evaluation scenarios

**Heidi Lam, Enrico Bertini, Petra Isenberg, Catherine Plaisant, Sheelagh Carpendale (2012), “Empirical Studies in Information Visualization: Seven Scenarios,” IEEE TVCG 18(9):1520–1536. DOI: 10.1109/TVCG.2011.279.**

Evaluation scenarios include visual data analysis/reasoning, user performance, user experience, work practices, communication, algorithms, and collaborative analysis.

**Skill implication:** evaluate the system according to its intended contribution; do not use a generic usability study for every visualization claim.

## 12. Scalable linked views

**Jeffrey Heer & Dominik Moritz (2024), “Mosaic: An Architecture for Scalable & Interoperable Data Views,” IEEE TVCG 30(1):436–446. DOI: 10.1109/TVCG.2023.3327189.**

Key contribution: interactive views publish declarative data needs coordinated through a shared query architecture, enabling scalable cross-filtering.

**Skill implication:** for large linked-view systems, separate data/query coordination from visual rendering.

## How to cite the engineering pattern

Do not write: “Research Visual Analytics Panel Design Pattern is an established theory.”

Prefer: “The interface design synthesizes task abstraction, visual encoding, interaction taxonomies, coordinated multiple views, and analytic provenance principles from established visualization research.”
