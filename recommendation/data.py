from tree import Tree

fps_games = [["Call of Duty: Modern Warefare 3", "FPS", 2023, "7/10"], ["Halo", "FPS", 2001, "8/10"], ["Fortnite", "FPS", 2017, "6/10"], ["Apex Legends", "FPS", 2019, "7/10"], ["Counter-Strike: 2", "FPS", "2023", "5/10"]]
rpg_games = [["World of Warcraft", "RPG", 2004, "8/10"], ["The Witcher 3: The Wild Hunt", "RPG", 2015, "9/10"], ["Elder Scrolls: Skyrim", "RPG", 2011, "10/10" ], ["Elden Ring", "RPG", 2022, "7/10"], ["Fallout 4", "RPG", 2015, "8/10"]]
plat_games = [["Shovel Knight", "Platformer", 2014, "4/10"],["Rayman Legends", "Platformer", 2011, "7/10"],["Super Marios 64", "Platformer", 1996, "9/10"],["Donkey Kong Country", "Platformer", 1994, "10/10"],["Cuphead", "Platformer", 2017, "7/10"]]
fighting_games = [["Street Fighter III: 3rd Strike", "Fighting", 2009, "10/10"],["Tekken 7", "Fighting", 2017, "8/10"],["Dragon Ball FighterZ", "Fighting", 2018, "7/10"],["Mortal Kombat", "Fighting", 2011, "6/10"],["Killer Instinct", "Fighting", 2011, "5/10"]]
survival_games = [["Minecraft", "Survival", 2011, "9/10"],["Valheim", "Survival", 2021, "8/10"],["Rust", "Survival", 2013, "6/10"],["Don't Starve", "Survival", 2013, "7/10"],["Subnautica", "Survival", 2014, "8/10"]]
simulation_games = [["Euro Truck Simulator 2", "Simulation", 2015, "4/10"],["Cities: Skylines", "Simulation", 2015, "9/10"],["The Sims 4", "Simulation", 2014, "9/10"],["PC Building Simulator", "Simulation", 2018, "10/10"],["Planet Coaster", "Simulation", 2016, "6/10"]]
racing_games = [["Forza Horizon 5", "Racing", 2021, "6/10"],["Mario Kart 8", "Racing", 2014, "9/10"],["Dirt 5", "Racing", 2020, "7/10"],["Burnout Paradise", "Racing", 2008, "9/10"],["Outrun", "Racing", 1986, "7/10"]]
rts_games = [["Age of Empires IV", "RTS", 2021, "7/10"],["Command & Conquer: Red Alert", "RTS", 2000, "9/10"],["Warcraft III: Reign of Choas", "RTS", 2002, "9/10"],["Starcraft II: Wings of Liberty", "RTS", 2010, "10/10"],["Warhammer 40,000: Dawn of War II", "RTS", 2009, "7/10"]]

list_of_lists = [fps_games, rpg_games, plat_games, fighting_games, survival_games, simulation_games, racing_games, rts_games]

potential_names = [["Shooter", "First Person", "Twitch", "FP", "FS"],
                   ["Role play", "Roleplaying", "Role", "MMORPG", "RP", "Leveling", "RGP"],
                   ["Plat", "Jumper", "Side scroll", "Puzzle"],
                   ["Beat em up", "Fighter", "Fight", "Boxing"],
                   ["Zombie", "Builder"],
                   ["Sim", "Pretend", "Life", "City", "Builder", "City Builder", "Mangement"],
                   ["Racer", "Dragracing", "Crash", "Speed"],
                   ["Real-time Strategy", "Strategy", "Real time", "Isometric", "Top down"]]
matching_potential = ["FPS", "RPG", "Platformer", "Fighting", "Survival", "Simulation", "Racing", "RTS"]

fps = Tree("FPS")
rpg = Tree("RPG")
plat = Tree("Platformer")
fight = Tree("Fighting")
surv = Tree("Survival")
sim = Tree("Simulation")
race = Tree("Racing")
rts = Tree("RTS")

fps1 = Tree(fps_games[0][0], fps_games[0][1], fps_games[0][2], fps_games[0][3])
fps2 = Tree(fps_games[1][0], fps_games[1][1], fps_games[1][2], fps_games[1][3])
fps3 = Tree(fps_games[2][0], fps_games[2][1], fps_games[2][2], fps_games[2][3])
fps4 = Tree(fps_games[3][0], fps_games[3][1], fps_games[3][2], fps_games[3][3])
fps5 = Tree(fps_games[4][0], fps_games[4][1], fps_games[4][2], fps_games[4][3])
###############################################################################
rpg1 = Tree(rpg_games[0][0], rpg_games[0][1], rpg_games[0][2], rpg_games[0][3])
rpg2 = Tree(rpg_games[1][0], rpg_games[1][1], rpg_games[1][2], rpg_games[1][3])
rpg3 = Tree(rpg_games[2][0], rpg_games[2][1], rpg_games[2][2], rpg_games[2][3])
rpg4 = Tree(rpg_games[3][0], rpg_games[3][1], rpg_games[3][2], rpg_games[3][3])
rpg5 = Tree(rpg_games[4][0], rpg_games[4][1], rpg_games[4][2], rpg_games[4][3])
###############################################################################
plat1 = Tree(plat_games[0][0], plat_games[0][1], plat_games[0][2], plat_games[0][3])
plat2 = Tree(plat_games[1][0], plat_games[1][1], plat_games[1][2], plat_games[1][3])
plat3 = Tree(plat_games[2][0], plat_games[2][1], plat_games[2][2], plat_games[2][3])
plat4 = Tree(plat_games[3][0], plat_games[3][1], plat_games[3][2], plat_games[3][3])
plat5 = Tree(plat_games[4][0], plat_games[4][1], plat_games[4][2], plat_games[4][3])
###############################################################################
fight1 = Tree(fighting_games[0][0], fighting_games[0][1], fighting_games[0][2], fighting_games[0][3])
fight2 = Tree(fighting_games[1][0], fighting_games[1][1], fighting_games[1][2], fighting_games[1][3])
fight3 = Tree(fighting_games[2][0], fighting_games[2][1], fighting_games[2][2], fighting_games[2][3])
fight4 = Tree(fighting_games[3][0], fighting_games[3][1], fighting_games[3][2], fighting_games[3][3])
fight5 = Tree(fighting_games[4][0], fighting_games[4][1], fighting_games[4][2], fighting_games[4][3])
###############################################################################
surv1 = Tree(survival_games[0][0], survival_games[0][1], survival_games[0][2], survival_games[0][3])
surv2 = Tree(survival_games[1][0], survival_games[1][1], survival_games[1][2], survival_games[1][3])
surv3 = Tree(survival_games[2][0], survival_games[2][1], survival_games[2][2], survival_games[2][3])
surv4 = Tree(survival_games[3][0], survival_games[3][1], survival_games[3][2], survival_games[3][3])
surv5 = Tree(survival_games[4][0], survival_games[4][1], survival_games[4][2], survival_games[4][3])
###############################################################################
sim1 = Tree(simulation_games[0][0], simulation_games[0][1], simulation_games[0][2], simulation_games[0][3])
sim2 = Tree(simulation_games[1][0], simulation_games[1][1], simulation_games[1][2], simulation_games[1][3])
sim3 = Tree(simulation_games[2][0], simulation_games[2][1], simulation_games[2][2], simulation_games[2][3])
sim4 = Tree(simulation_games[3][0], simulation_games[3][1], simulation_games[3][2], simulation_games[3][3])
sim5 = Tree(simulation_games[4][0], simulation_games[4][1], simulation_games[4][2], simulation_games[4][3])
###############################################################################
race1 = Tree(racing_games[0][0], racing_games[0][1], racing_games[0][2], racing_games[0][3])
race2 = Tree(racing_games[1][0], racing_games[1][1], racing_games[1][2], racing_games[1][3])
race3 = Tree(racing_games[2][0], racing_games[2][1], racing_games[2][2], racing_games[2][3])
race4 = Tree(racing_games[3][0], racing_games[3][1], racing_games[3][2], racing_games[3][3])
race5 = Tree(racing_games[4][0], racing_games[4][1], racing_games[4][2], racing_games[4][3])
###############################################################################
rts1 = Tree(rts_games[0][0], rts_games[0][1], rts_games[0][2], rts_games[0][3])
rts2 = Tree(rts_games[1][0], rts_games[1][1], rts_games[1][2], rts_games[1][3])
rts3 = Tree(rts_games[2][0], rts_games[2][1], rts_games[2][2], rts_games[2][3])
rts4 = Tree(rts_games[3][0], rts_games[3][1], rts_games[3][2], rts_games[3][3])
rts5 = Tree(rts_games[4][0], rts_games[4][1], rts_games[4][2], rts_games[4][3])

fps.add_child(fps1), fps.add_child(fps2), fps.add_child(fps3), fps.add_child(fps4), fps.add_child(fps5)
rpg.add_child(rpg1), rpg.add_child(rpg2), rpg.add_child(rpg3), rpg.add_child(rpg4), rpg.add_child(rpg5)
plat.add_child(plat1), plat.add_child(plat2), plat.add_child(plat3), plat.add_child(plat4), plat.add_child(plat5)
fight.add_child(fight1), fight.add_child(fight2), fight.add_child(fight3), fight.add_child(fight4), fight.add_child(fight5)
surv.add_child(surv1), surv.add_child(surv2), surv.add_child(surv3), surv.add_child(surv4), surv.add_child(surv5)
sim.add_child(sim1), sim.add_child(sim2), sim.add_child(sim), sim.add_child(sim4), sim.add_child(sim5)
race.add_child(race1), race.add_child(race2), race.add_child(race3), race.add_child(race4), race.add_child(race5)
rts.add_child(rts1), rts.add_child(rts2), rts.add_child(rts3), rts.add_child(rts4), rts.add_child(rts5)

master_tree = Tree("Master")
master_tree.add_child(fps), master_tree.add_child(rpg), master_tree.add_child(plat), master_tree.add_child(fight)
master_tree.add_child(surv), master_tree.add_child(sim), master_tree.add_child(race), master_tree.add_child(rts)
