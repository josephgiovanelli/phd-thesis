# Ph.D. - Thesis

![Build](https://travis-ci.com/w4bo/phd-thesis.svg?token=eCxgQzWEteuAmE58GzVG&branch=master)

Building the thesis
    
    ./gradlew buildLatex

Cleaning the references: (i) remove unused .bib and (ii) get the duplicated .bib under different names

- In Latex, uncomment `refcheck` in `global/packages.tex`
- Run `scripts/clean_bib.sh`

## TODO

- Notes on slides:
  - Avoid saying "Quello che è"
  - Smooth augmented OLAP and related works
  - Fix conclusions with something to wrap-up what has been done
  - Fix the context in the big data slides
  - Introduce the "personal gazetteer"
- Da commenti Stefano:
  - As to vs As for (As for scalability)
- To ask:
    - (x) From OLTP, to OLAP, to OLAM, to Expert Systems ?? What are expert systems?
        - Data           -> Operational database, OLTP
        - Information    -> DW, OLAP
        - Knowledge      -> (Pattern base) Machine learning, Data mining, OLAM
        - Expert systems -> E' un termine vecchio e in disuso, meglio usare "Decisions and Actions"
    - (x) A-BI and not A-OLAP, although the title is now "Augmented OLAP"
    - (x) Togliere la sezione per il size "k" da describe
- Title: Knowledge pyramid
    - (x) "Preamble" --> "The knowledge pyramid"
    - (x) In base al titolo rivedere abstract
    - (x) Le due parti devono essere sinergiche
    - (x) In OLAP aggiungere riferimento a framework principale
- Conclusion
    - (x) Keep (local) conclusion in each chapter. "We implemented this .... The results are ..."
    - (x) Add conclusion at the end of each part
- Slides (20 minutes)
    - (x) 10 minutes on the introduction, the one case study for each part

- \emph{} la prima volta che introduco un termine
- Check dei miei paper citati
    - Aggiungere riferimento a story telling e CUT
- Make section names consistent
    - Related works
    - Conclusion
    - ...

### Grammar checks and regex

What to check:

    - (x) Authors -> The Authors
    - Pay attention to the articles
    - (x) wide-spreading vs wide spreading vs widespreading
    - (x) On-Line Analytical Processing
    - (x) business intelligence
    - (x) spatiotemporal vs spatio-temporal
    - paper/survey/review/work -> chapter
    - On one hand -> On the one hand
    - Quotes should be `` '' and not "
    - White upper case after dot `[.]\s+[a-z]`
    - White spaces after dot `[.][a-z]`
    - White spaces after comma `,[a-z]`

Colocations:

    - inspired by
    - divide into
    - competence in

## Template

Template taken from [here](http://www-h.eng.cam.ac.uk/help/tpl/textprocessing/ThesisStyle/)
