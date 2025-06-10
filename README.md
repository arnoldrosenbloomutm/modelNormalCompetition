# modelNormalCompetition
Using python we model a collection of competitors, each with their own normal distribution around their abilities.

When competitor i and j compete, their current ability is chosen from N(mu_i, sigma_i) and N(mu_j,sigma_j).
The one with the higher ability for the competition wins the competition. Now the goal of all of this is to see if, after
repeated competitions, the system can derive the mu_i, sigma_i which best explains the sequence of competitions.

The system here provides the competitors with all of their initial mu, sigma, the arena for repeated competitions
and finally the system that, having observed the competitions and the winners, using baysean inference, tries to derive mu_i and sigma_i
which explains the observed simulation. 

The derived mu_i, sigma_i do not necessarily match the original, but if we replay the competitions with the derived mu_i, sigma_i
many of the outcomes should be the same.
