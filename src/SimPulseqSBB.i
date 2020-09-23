// SimPulseqSBB.i

%module SimPulseqSBB

%{
#define SWIG_FILE_WITH_INIT
#include "SimPulseqSBBTemplate.h"
//#include "BlochMcConnellSolver.h"
#include <functional>
#include <numeric>
#include <vector>
#include "3rdParty/Eigen/Eigen"
//using namespace Eigen;
#include "SimulationParameters.h"
#include "SimPulseqSBB.h"
//typedef  SimulationParameters
#include "ExternalSequence.h"
#define _USE_MATH_DEFINES
#include <cmath>

%}

%include "eigen.i"
%include "SimulationParameters.cpp"
%include "SimulationParameters.h"
%include "SimPulseqSBB.cpp"
//%include "SimPulseqSBBTemplate.h"
//%template(SimPulseqSBBT) SimPulseqSBBTemplate<int>;
// using namespace Eigen;




