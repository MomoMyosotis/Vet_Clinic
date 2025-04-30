-- first line

-- si usa una query per riempire la tabella con gli obj illness

-- Inserimento delle malattie con i dati richiesti

INSERT INTO illness (name, description, cure, lethality, life_cycles)
VALUES
    ('Sonnite acuta', 'Infiammazione acuta delle vie respiratorie', 'Riposo e antibiotici', FALSE, 1),
    ('Flammable fur', 'Pelo altamente infiammabile', 'Controllo ambientale', TRUE, 2),
    ('Existential dread', 'Ansia esistenziale', 'Terapia cognitivo-comportamentale', FALSE, 3),
    ('Mania acuta', 'Disturbo mentale con sintomi di esaltazione e impulsività', 'Farmaci stabilizzatori dell’umore', TRUE, 4),
    ('Needs constant supervision', 'Necessità di sorveglianza continua', 'Monitoraggio costante', FALSE, 5),
    ('Hyperactive', 'Comportamento iperattivo', 'Controllo comportamentale', FALSE, 2),
    ('Alive and dead', 'Condizione di apparente morte temporanea', 'Monitoraggio medico', TRUE, 6),
    ('Joint issues', 'Problemi alle articolazioni', 'Farmaci antinfiammatori', FALSE, 3),
    ('Mild conspiracy tendencies', 'Tendenze paranoiche e sospettose', 'Terapia psicologica', FALSE, 1),
    ('Aggressively patriotic', 'Comportamento estremamente patriottico', 'Supporto psicologico', FALSE, 2),
    ('Addicted to heavy metal', 'Dipendenza da musica heavy metal', 'Terapia di disintossicazione musicale', FALSE, 3),
    ('Dancer at heart', 'Amore per la danza', 'Nessuna cura necessaria', FALSE, 4),
    ('Dreams of the ocean', 'vuole vivere nel mare', 'Supporto psicologico', FALSE, 2),
    ('Loves to explore', 'Ama esplorare', 'Nessuna cura necessaria', FALSE, 5),
    ('Is afraid of rain', 'Paura intensa della pioggia', 'Terapia psicologica', FALSE, 2),
    ('Not of this world', 'Comportamento alienante e distacco dalla realtà', 'Supporto psicologico', TRUE, 7),
    ('Electrified fur', 'Pelo che genera scariche elettriche', 'Isolamento dal campo elettrico', TRUE, 2),
    ('Master of flips', 'Capacità di eseguire acrobazie in modo perfetto', 'Nessuna cura necessaria', FALSE, 3),
    ('peachy', 'Condizione psicologica di benessere e tranquillità', 'Relax e meditazione', FALSE, 1);



-- last line