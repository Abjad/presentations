# -*- coding: utf-8 -*-
# tools first, materials second, segments last:
# makes it possible for materials to import tools;
# makes it possible for segments to import both materials and tools.
from trio_score import tools
from trio_score import materials
from trio_score import segments
