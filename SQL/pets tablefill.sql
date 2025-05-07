-- first line

INSERT INTO pets(name, species, age, peso, height, stato, owner_id)
VALUES
    ('Pollosauro', 'Nooty', 1.2, 120, 30, 't', 'MY050T1S'),
    ('Sonnus canis', 'bianca', 20, 30, 100, 'f', 'P4P4V3R1'),
    ('strambus selvaticus', 'weirdass thing', 911, 84, 69, 't', 'G1R450L1'),
    ('Felis combustibilis', 'Zampa', 3, 5.5, 45, 'f', 'C1CL4M1N1'),
    ('Canis depressus', 'Tristezza', 7, 20, 80, 'f', 'M4RGH3R1T4'),
    ('Capra lunatica', 'Becky la Svitata', 5, 32, 60, 'f', 'L0T0814NC0'),
    ('Draconis minus', 'Pufflet', 0.4, 1.2, 25, 'f', 'P4P4V3R1'),
    ('Tartaruga turbo', 'Nitro', 80, 70, 90, 'f', 'M4RGH3R1T4'),
    ('Gatto quantico', 'Schrödy', 2, 3, 40, 't', 'MY050T1S'),
    ('Cane a molla', 'Slinky', 1, 8, 50, 'f', 'P4P4V3R1'),
    ('Coniglius paranoicus', 'Twitch', 6, 4.2, 30, 't', 'G1R450L1'),
    ('Topus gladiator', 'Spartacchio', 0.9, 0.8, 20, 't', 'C1CL4M1N1'),
    ('Cacatua metallum', 'Rocky', 10, 12, 55, 't', 'M4RGH3R1T4'),
    ('Leone Ballerino', 'Rex', 200, 250, 120, 't', 'P1L4V3L0'),
    ('Squalo Sognante', 'Sharky', 1500, 800, 600, 't', 'G4L123V'),
    ('Cervo Curioso', 'Bambi', 20, 200, 150, 't', 'S3TA1C0'),
    ('Cane Nube', 'Cloudy', 9, 20, 65, 't', 'F4NC3S9'),
    ('Gatto Cosmico', 'Nebula', 4, 4, 45, 't', 'P1L4V3L0'),
    ('Tigre Elettrica', 'Volt', 300, 220, 180, 't', 'S3TA1C0'),
    ('Foca Acrobatica', 'Flippy', 70, 100, 150, 't', 'G4L123V'),
    ('peachy penguosus', 'pingu', 10, 2, 40, 'f', 'P4P4V3R1')

ON CONFLICT (id) DO NOTHING


-- last line