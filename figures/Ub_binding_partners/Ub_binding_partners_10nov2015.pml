#Pymol .pml script to visualize ubiquitin binding partners

# reinitialize the program
reinit

# set the viewing region
viewport 500, 500

# download pdb files
# 1ubq is for ubiquitin, the other pdb files are complexes of ubiquitin and its binding partners 
fetch 1ubq, async = 0
fetch 4lcd, async = 0 
fetch 1fxt, async = 0 
fetch 3k9p, async = 0 

# set background color to white
# show proteins as a cartoon
bg white
as cartoon

# align each ubiquitin complex to the ubiquitin from 1ubq
align 4lcd and chain e, 1ubq
align 3k9p and chain b, 1ubq
align 1fxt and chain b, 1ubq

# select just ubiquitin
select ub, bc. (1ubq around .2)

# select binding partners that interact with uqibuitin
select 4lcd_other_chain, bc. 4lcd and (ub around 4)
select 3k9p_other_chain, bc. 3k9p and (ub around 4)
select 1fxt_other_chain, bc. 1fxt and (ub around 4)

# select specific residues that interact with ubiquitin
select 4lcd_nearby, br. 4lcd_other_chain and (ub around 1.3)
select 3k9p_nearby, br. 3k9p_other_chain and (ub around 1.3)
select 1fxt_nearby, br. 1fxt_other_chain and (ub around 1.3)

# display interacting residues as spheres
show spheres, 4lcd_nearby and n. CA
show spheres, 3k9p_nearby and n. CA
show spheres, 1fxt_nearby and n. CA

# show binding surface on ubiquitin
# show surface, 4lcd and chain e and (4lcd_nearby around 5)
# show surface, 3k9p and chain b and (3k9p_nearby around 5)
# show surface, 1fxt and chain b and (1fxt_nearby around 5)
# 
# color binding surfaces by each different binding partner
# set surface_color, aqua, (4lcd and chain e)
# set surface_color, orange, (3k9p and chain b)
# set surface_color, pink, (1fxt and chain b)
# 
# make surfaces transparent
# set transparency, 0.5, (4lcd and chain e)
# set transparency, 0.5, (3k9p and chain b)
# set transparency, 0.5, (1fxt and chain b)
# 
# show surface of just ubiquitin
# show surface, 1ubq
# set surface_color, white, 1ubq
# set transparency, 0.5, 1ubq
# hide cartoon, 1ubq

# color each ubiquitin in each pdb gray
color gray70, (4lcd and chain e)
color gray70, (3k9p and chain b)
color gray70, (1fxt and chain b)

# center figure and prepare it for presentation
orient 1ubq

hide cartoon
show cartoon, 4lcd and chain e
show cartoon, 3k9p and chain b
show cartoon, 1fxt and chain b

select none
ray

# show just 4lcd
disable 
enable 4lcd
scene 4lcd, store

# show just 3k9p
disable 
enable 3k9p
scene 3k9p, store

# show just 1fxt
disable 
enable 1fxt
scene 1fxt, store

# make slideshow showing the three ubiquitin binding partners
# manually, go to Movie --> Program --> Scene loop --> Steady --> 2 seconds each

# commands
#mset('1x1')
#set('scene_loop')
#set('movie_fps', 1.0 / 5.0)
#mdo(1, 'scene auto, next')
mplay()

