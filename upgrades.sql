INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3, value_tier_4, name_tier_4, value_tier_5, name_tier_5,
    cost_tier_1, cost_tier_2, cost_tier_3, cost_tier_4, cost_tier_5,
    description_tier_1, description_tier_2, description_tier_3, description_tier_4, description_tier_5
    ) 
VALUES (
    'pickaxe', 'ADD', 5, 'Iron Pickaxe', 10, 'Bronze Pickaxe', 15, 'Steel Pickaxe', 20, 'Mithril Pickaxe', 30, 'Qubit Pickaxe',
    25, 250, 1000, 10000, 120000,
    'A basic pickaxe made of unalloyed iron. Increases base point gain',
    'A pickaxe made of bronze. Slightly better than basic iron',
    'A good quality steel pickaxe. Most employees use it due to its reliability',
    'A pickaxe made of the legendary mithril. Highly enchanted',
    'A pickaxe made from fragments of The Cube. Nobody else has one remotely similar'
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3,
    cost_tier_1, cost_tier_2, cost_tier_3,
    description_tier_1, description_tier_2, description_tier_3
    ) 
VALUES (
    'lantern', 'MULTIPLY', 1.5, 'Gas Lamp', 2, 'Electric Lantern', 3, 'Flashlight',
    100, 1500, 50000,
    'A low-quality gas lamp. Being able to see increases your ability to mine by a lot.',
    'A lantern powered by batteries. More reliable than the gas lamp',
    'A more convenient version of the lantern. A lot smaller and efficient.'
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3,
    cost_tier_1, cost_tier_2, cost_tier_3,
    description_tier_1, description_tier_2, description_tier_3
    ) 
VALUES (
    'assistant', 'PASSIVE', 5, 'Elves', 10, 'Gnomes', 20, 'Dwarves',
    100, 1500, 100000,
    'Elven assistants to mine even when you are not. They are weak',
    'Gnomes are a lot better at mining than elves. But so are most people',
    'Dwarves are born for the mines. Rock and Stone!'

);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1, description_tier_1
    ) 
VALUES (
    'meals', 'EXPONENT', 1.1, 'Regular Meals', 1000, 
    'Being able to reliably feed yourself allows for more time at the mine before getting tired.'
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1, description_tier_1
    ) 
VALUES (
    'housing', 'EXPONENT', 1.1, 'Good Housing', 10000,
    'A better place to sleep. Better sleep means less sleep needed'
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1, description_tier_1
    ) 
VALUES (
    'helmet', 'MULTIPLY', 1.5, 'Mining Helmet', 5000, 
    'A helmet with a weak flashlight. Safety First!'
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1, description_tier_1
    ) 
VALUES (
    'cartographer', 'MULTIPLY', 3, 'Cartographer Assistant', 200000,
     'A good cartographer allows for less getting lost in the labyrinthine tunnels that reach the cube'
);
INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1, description_tier_1
) VALUES (
    'winning_condition', 'VICTORY', 0, 'Anti-CUBE Explosives', 1000000, 
    'The Cube shall know pain.'
);