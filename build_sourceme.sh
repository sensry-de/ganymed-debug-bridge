#!/bin/bash
#
# Copyright (C) Fraunhofer-Institut for Photonic Microsystems (IPMS)
# Maria-Reiche-Str. 2
# 01109 Dresden
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# 
# \author phil.seipt@ipms.fraunhofer.de
# \date 06.02.2019

if [ ! -d "bin" ]; then
  echo "Directory bin not found."
  echo "Execute script from origin directory"
  exit 1
fi

if [ ! -d "configs" ]; then
  echo "Directory configs not found."
  echo "Execute script from origin directory"
  exit 1
fi

if [ ! -d "python" ]; then
  echo "Directory python not found."
  echo "Execute script from origin directory"
  exit 1
fi

if [ -f "sourceme.sh" ]; then
  echo Deleting old sourceme.sh
  rm sourceme.sh
fi
touch sourceme.sh


printf "Generating sourceme.sh ..."

printf "export PATH=" >>sourceme.sh
pwd | tr -d '\n' >>sourceme.sh
printf "/bin:\$PATH\n" >>sourceme.sh

printf "export PYTHONPATH=" >>sourceme.sh
pwd | tr -d '\n' >>sourceme.sh
printf "/python:\$PYTHONPATH\n" >>sourceme.sh

printf "export LD_LIBRARY_PATH=" >>sourceme.sh
pwd | tr -d '\n' >>sourceme.sh
printf "/lib:\$LD_LIBRARY_PATH\n" >>sourceme.sh

printf "export PULP_CONFIGS_PATH=" >>sourceme.sh
pwd | tr -d '\n' >>sourceme.sh
printf "/python\n" >>sourceme.sh

printf "DONE\n"

exit 0
