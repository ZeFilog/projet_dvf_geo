# projet_dvf_geo
Le fichier DVF (Demandes de Valeurs Foncières) produit par le 'Ministère de l'Économie,
des Finances et de la Souveraineté industrielle et numérique' est maintenant accessible en
open data, en conformité avec un décret de décembre 2018 relatif à la publication
électronique d'informations sur les valeurs foncières déclarées lors de mutations
immobilières. La publication de ces informations vise à rendre les marchés fonciers et
immobiliers plus transparents. Le fichier comportant des informations à caractère personnel,
son utilisation nécessite certaines précautions :
1. ne doit pas permettre de ré-identifier les personnes concernées, de manière indirecte
2. ne doit pas permettre l'indexation des informations sur les moteurs de recherche


Ce jeu de données "Demandes de valeurs foncières", publié par la DGFiP, recense les
transactions immobilières des 5 dernières années en métropole et DOM-TOM (sauf Alsace,
Moselle et Mayotte). Les informations sont tirées des actes notariés et des données
cadastrales.

Une documentation détaillée comportant 'Foire aux questions', Conditions générales
d'utilisation', 'Information des personnes concernées par le traitement informatique' et
'Notice descriptive des fichiers de valeurs foncières' est accessible via le site
https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/#resources. Elle permet
notamment de comprendre, à travers leur description détaillée, les champs renseignés et les
données présentes dans la base de données mais aussi toute information relative à
l'utilisation de la base.

Le premier jeu de données que nous avons utilisé dans le cadre de notre projet est dérivé du
fichier DVF. Les fichiers sont produits par Etalab (département de la Direction Interministérielle
du Numérique qui coordonne la conception et la mise en œuvre de la stratégie d'open data de
l’État) dans un format normalisé et enrichi. Nous avons récupéré ces données dans des fichiers
aux formats csv.

Des informations détaillées concernant les enrichissements faits par rapport à la base de
données initiales ainsi que d'autres informations complémentaires peuvent être trouvées à
cette adresse
https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/.

Le second jeu de données que nous avons utilisé a été produit par Rennes Métropole. Les
données disponibles dans plusieurs formats à cette adresse
https://geo.data.gouv.fr/fr/datasets/63a0ef5654cb7cf3e28684e6b7dc7ca84eaf9799 ont été
mises à jour jusqu'en 2021. Une documentation succincte présente sur le site nous indique
que les données sont des données géospatiales décrivant par des polygones les bâtiments de
3
Rennes Métropole.
Les bâtiments possèdent un identifiant unique composé d'un digramme
(code commune + suite de 6 caractères numériques) et sont décrits par des points
géolocalisés. Les données ont été collectées à partir des permis de construire (Ville de
Rennes), de bases topographiques et orthophotographiques ou de restitution
photogrammétrique. L'objectif de la constitution d'une telle base était de maintenir une base
de référence locale pour les besoins de la ville. Rennes Métropole, précurseure de l'open data,
la base créée en 2005 avait aussi pour objectif d'être mise à jour plus fréquemment que les
sources de données externes comme la DGFiP. Nous avons utilisé le fichier dans son format
geoJSON.
