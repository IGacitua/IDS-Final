INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3, value_tier_4, name_tier_4, value_tier_5, name_tier_5,
    cost_tier_1, cost_tier_2, cost_tier_3, cost_tier_4, cost_tier_5
    ) 
VALUES (
    'pickaxe', 'ADD', 5, 'Iron Pickaxe', 10, 'Bronze Pickaxe', 15, 'Steel Pickaxe', 20, 'Mithril Pickaxe', 30, 'Qubit Pickaxe',
    50, 250, 1000, 10000, 50000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3,
    cost_tier_1, cost_tier_2, cost_tier_3
    ) 
VALUES (
    'lantern', 'MULTIPLY', 1.2, 'Gas Lamp', 1.5, 'Electric Lantern', 2, 'Flashlight',
    100, 1500, 3000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, value_tier_2, name_tier_2, value_tier_3, name_tier_3,
    cost_tier_1, cost_tier_2, cost_tier_3
    ) 
VALUES (
    'assistant', 'PASSIVE', 5, 'Elves', 10, 'Gnomes', 20, 'Dwarves',
    500, 2000, 10000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1
    ) 
VALUES (
    'meals', 'EXPONENT', 1.1, 'Regular Meals', 1000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1
    ) 
VALUES (
    'housing', 'EXPONENT', 1.1, 'Good Housing', 5000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1
    ) 
VALUES (
    'helmet', 'MULTIPLY', 1.5, 'Mining Helmet', 2000
);

INSERT INTO upgrades (
    internal_name, effect, value_tier_1, name_tier_1, cost_tier_1
    ) 
VALUES (
    'cartographer', 'MULTIPLY', 3, 'Cartographer Assistant', 200000
);