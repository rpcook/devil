# devil
This is a quick and dirty set of code to help visualise the solution to an old riddle. Requires pygame.

The Riddle:
Because reasons, you find yourself facing the devil. He challenges you to a challenge for your immortal soul (of course).

Before you both is a round table (more advanced telling of this riddle can have an arbitrary shaped table, provided that it has even order rotational symmetry), beside you both is a pile of identical round coins. The game is to place a coin on the table, in turn, until you can no longer fit a coin onto the table. The rules are:
  - No overlapping of the coins
  - No moving coins that are already placed
  - All coins must be placed entirely on the table (no hanging off the edge)
  - Size of coins and table are arbitrary and fixed for the duration of the challenge.

The devil generously lets you go first (how kind). 

The question is: is there a strategy that guarantees that you will keep your immortal soul?

Bonus question: can you explain why?

Solution is on line 100...
















































































SOLUTION (spoilers, duh):
1. Place your first coin in the exact centre of the table.
2. The devil will then place a coin at some other location (if available, if not he loses, you keep your soul).
3. Place your next coin at the mirror-image position to the last coin the devil placed. I.e. at the same distance from the centre along the same diameter.
4. GoTo 2.

Why:
As the table is round (or even order rotationally symmetric), placing your first coin at the centre forces the devil to play at a position that must have an empty spot at the same radial distance along the same diameter. You then have a guaranteed free spot to play your next coin in. Eventually the table won't have a space for the devil's coin as this strategy means you always have space.
