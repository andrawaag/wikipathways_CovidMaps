## WikiPathways API calls as SPARQL queries

### listOrganisms
source: [listOrganisms](https://webservice.wikipathways.org/ui/#!/All_functions/get_listOrganisms)
```sparql
# listOrganisms: https://webservice.wikipathways.org/ui/#!/All_functions/get_listOrganisms
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>

SELECT DISTINCT ?organism
WHERE {
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:organismName ?organism .
    }
}
```
[Try me...](https://w.wiki/5oau)

### listPathways
source: [listPathways](https://webservice.wikipathways.org/ui/#!/All_functions/get_listPathways)
```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?wpuri ?title ?wpid
WHERE {
    VALUES ?organism {"Homo sapiens"}
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:organismName ?organism ;
                 dct:identifier ?wpid ;
                 dce:identifier ?wpuri ;
                 dce:title ?title .
    }
}
```
[Try me...](https://w.wiki/5oay)

### getPathway
source: [getPathway](https://webservice.wikipathways.org/ui/#!/All_functions/get_getPathway)
#### Not optimal 
This API returns the pathways in a select set of output formats. Downloading these renderings is not optimal with SPARQL

### getPathwayInfo
source: [getPathwayInfo](https://webservice.wikipathways.org/ui/#!/All_functions/get_getPathwayInfo)
```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?wpuri (uri(concat("https://www.wikipathways.org/index.php/Pathway:", ?wpid)) as ?wpurl) (STRAFTER(str(?pathway), "_") as ?revision) ?title ?wpid ?organism
WHERE {
    VALUES ?wpid {"WP716"}
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:organismName ?organism ;
                 dct:identifier ?wpid ;
                 dce:identifier ?wpuri ;
                 wp:organismName ?organism ;
                 dce:title ?title .
    }
}
```
[Try me...](https://w.wiki/5ocb)

### getPathwayHistory
source: [getPathwayHistory](https://webservice.wikipathways.org/ui/#!/All_functions/get_getPathwayHistory)
#### comment
The SPARQL endpoint only has last released version. History is not part of the endpoint.
### getRecentChanges
source: [getRecentChanges](https://webservice.wikipathways.org/ui/#!/All_functions/get_getRecentChanges)
#### comment
The SPARQL endpoint only has last released version. Recent changes are not part of the endpoint.

### login
#### comment
Not supported

### getPathwayAs
#### comment
Not supported
###updatePathway
#### comment
Not supported
### createPathway
#### comment
Not supported

### findPathwaysByText

GET /findPathwaysByXref
### removeCurationTag
#### comment
Not supported
### saveCurationTag
#### comment
Not supported
GET /getCurationTags
GET /getCurationTagsByName
### getCurationTagHistory
#### comment
Not supported
### getColoredPathway
#### comment
Not supported
GET /findInteractions
GET /getXrefList
GET /findPathwaysByLiterature
### saveOntologyTag
#### comment
Not supported
### removeOntologyTag
#### comment
Not supported
### getOntologyTermsByPathway
source: [getOntologyTermsByPathway](https://webservice.wikipathways.org/ui/#!/All_functions/get_getOntologyTermsByPathway)
```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?wpuri (uri(concat("https://www.wikipathways.org/index.php/Pathway:", ?wpid)) as ?wpurl) (STRAFTER(str(?pathway), "_") as ?revision) ?title ?wpid ?ontologyTag ?ontologyTagLabel 
WHERE {
    VALUES ?wpid {"WP716"}
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:ontologyTag ?ontologyTag ;
                 dct:identifier ?wpid ;
                 dce:identifier ?wpuri ;
                 dce:title ?title .
      ?ontologyTag rdfs:label ?ontologyTagLabel .
    }
}
```
[Try me...](https://w.wiki/5od$)

### getPathwaysByOntologyTerm
source: [getPathwaysByOntologyTerm](https://webservice.wikipathways.org/ui/#!/All_functions/get_getPathwaysByOntologyTerm)
```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>
PREFIX obo: <http://purl.obolibrary.org/obo/>

SELECT DISTINCT ?wpuri (uri(concat("https://www.wikipathways.org/index.php/Pathway:", ?wpid)) as ?wpurl) (STRAFTER(str(?pathway), "_") as ?revision) ?title ?wpid ?ontologyTag ?ontologyTagLabel 
WHERE {
    VALUES ?ontologyTag {obo:PW_0000141}
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:ontologyTag ?ontologyTag ;
                 dct:identifier ?wpid ;
                 dce:identifier ?wpuri ;
                 dce:title ?title .
      ?ontologyTag rdfs:label ?ontologyTagLabel .
    }
}
```
[Try me...](https://w.wiki/5oe5)

### getPathwaysByParentOntologyTerm
source: [getPathwaysByParentOntologyTerm](https://webservice.wikipathways.org/ui/#!/All_functions/get_getPathwaysByParentOntologyTerm)

```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX wp: <http://vocabularies.wikipathways.org/wp#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>
PREFIX obo: <http://purl.obolibrary.org/obo/>

SELECT DISTINCT ?wpuri (uri(concat("https://www.wikipathways.org/index.php/Pathway:", ?wpid)) as ?wpurl) (STRAFTER(str(?pathway), "_") as ?revision) ?title ?wpid   
WHERE {
    VALUES ?ontologyTag {obo:PW_0000002}
    SERVICE <http://sparql.wikipathways.org/sparql> {
        ?pathway wp:ontologyTag+ ?ontologyTag ;
                 dct:identifier ?wpid ;
                 dce:identifier ?wpuri ;
                 dce:title ?title .
    }
}
```
[Try me...](https://w.wiki/5ofd)

### getUserByOrcid

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dce: <http://purl.org/dc/elements/1.1/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT * 
WHERE {
    VALUES ?orcid {"0000-0001-9773-4008"}
    bind (uri(concat("https://orcid.org/", ?orcid)) as ?orciduri) 
                    
    SERVICE <http://sparql.wikipathways.org/sparql> {
      ?curator rdf:type foaf:Person ;
               dce:identifier ?orciduri .
    }
}
```
[Try me...](https://w.wiki/5oeT)
### getPathwaysByOrcid
#### comment
extra
```sparql

PREFIX dce: <http://purl.org/dc/elements/1.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT * 
WHERE {
    VALUES ?orcid {"0000-0001-9773-4008"}
    bind (uri(concat("https://orcid.org/", ?orcid)) as ?orciduri) 
                    
    SERVICE <http://sparql.wikipathways.org/sparql> {
        
      ?pathway dce:creator ?curator .
      ?curator rdf:type foaf:Person ;
               dce:identifier ?orciduri .
    }
}
```
[Try me...](https://w.wiki/5oeV)
