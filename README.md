# cern_antimatter_sonification

In diesem Projekt wird ein Datensatz sonifiziert, der aus dem LHCb-Experiment (Large Hadron Collider beauty) am CERN stammt. Eines der Ziele des LHCb-Experiments sind Erkenntnisse bezüglich der CP-Violation zu sammeln. CP-Violation meint die unaufgeklärte Asymmetrie zwischen Materie und Antimaterie in unserem Universum. Obwohl im Universum die selbe Menge an Materie existieren sollte, wie an Antimaterie, besteht ein Großteil des bekannten Universums aus Materie. Die Antimaterie enthält die selben Quanten-Teilchen wie die Materie, jedoch mit jeweils entgegengesetzter Ladung. 
In dem verwendeten Datensatz werden die Unterschiede zwischen B+ und B- Mesonen untersucht. B-Mesonen bestehen aus einem Quark und einem Antiquark. B-Mesonen haben eine sehr kurze Lebenszeit, weswegen sie nicht in dem LHCb-Detektor des CERNs erfasst werden können. Stattdessen werden deren Zerfallsprodukte erfasst, dessen Lebenszeiten lang genug für eine Erfassung ist. Ein B+ Meson hat eine Ladung von +1, besteht aus einem Up-Quark und einem Anti-Beauty-Quark und zerfällt in zwei positiv geladene Kaonen und einem negativ geladenen Kaon. Ein B- Meson hingegen hat eine Ladung von -1, besteht aus einem positiv geladenen Kaon und zwei negativ geladenen Kaonen.
Aus Informationen der Kaonen können Rückschlüsse auf B-Mesonen geführt werden.
Beispielsweise kann der Impuls und damit die Energie eines Teilchens aus den im Datensatz enthaltenen Magnituden in X-, Y-, und Z-Richtung berechnet werden. Kennt man den Impuls aller in einem Event enthaltenen Kaonen, kann man damit auf den Impuls und die Energie des B-Mesons rückschließen.
Nicht jedes Event oder jede Reihe in dem Datensatz repräsentieren drei Kaonen, sondern können auch Pionen oder Myonen enthalten. Falls die Teilchen in einem Event Pionen oder Myonen enthalten, darf angenommen werden, dass die Teilchen des Events kein Zerfallsprodukt eines B-Mesons sind.

Für die Sonifikation des Datensatzes wurde zunächst ein Python-Skript (cern_data_processing.py) erstellt, dass eine Kopie eines Ausschnitts des Originaldatensatzes erstellt. Mithilfe der Pandas-Library wurden zu dem Dataframe der Kopie Spalten hinzugefügt, die die errechneten Impulse der drei Teilchen einer Reihe, die daraus resultierende Energie der einzelnen Teilchen, der Impuls eines potentiellen B-Mesons, sowie die Energie eines möglichen B-Mesons enthalten. Da in dem Originaldatensatz sehr selten ein Event mit drei Kaonen vorkommt, aber diese für die Sonifikation klanglich stärker mit Events mit Pionen oder Myonen gegenübergestellt werden sollen, wurde ein Dataframe mit 300 zufälligen Events erstellt und daraufhin Events mit circa 30 preselektierten Kaonen-Events an zufällige Indizes angeordnet.
Dieser Dataframe wird Reihe für Reihe jeweils über OSC an Max/MSP übermittelt.
Um das Python-Skript ausführen zu können, muss zunächst die Library [Uproot]([Uproot](https://uproot.readthedocs.io/en/latest/index.html)) installiert werden . Beispielsweise über:
``` pip install uproot awkward```

Um das Python-Skript zu starten muss folgender Befehl ausgeführt werden:
``` python cern_data_processing.py ```
Es dauert circa 300 - 400 Sekunden bis der komplette Dataframe über OSC übermittelt wurde .

## Max-Patches



Gerenderte Beispielergebnisse wurden in diesem 
