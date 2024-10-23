#########################
Installation instructions
#########################

Installing a pre-built package
======================================


.. rubric:: Installing via conda

The `conda-forge <http://anaconda.org/conda-forge/cvxopt>`_ channel
provides pre-built CVXOPT packages for Linux, macOS, and Windows that can be
installed using `conda <https://conda.io/docs/>`_::

	conda install -c conda-forge cvxopt

These pre-built packages are linked against OpenBLAS and
include all the optional extensions (DSDP, FFTW, GLPK, and GSL).

.. rubric:: Installing via pip

A pre-built binary wheel package can be installed
using `pip <https://pip.pypa.io>`_::

	pip install cvxopt

Wheels for Linux:

* are available for Python 3.7-3.13
* are linked against OpenBLAS
* include all optional extensions (DSDP, GLPK, GSL, and FFTW)

Wheels for macOS:

* are available for Python 3.7-3.13
* are linked against OpenBLAS
* include all optional extensions (DSDP, GLPK, GSL, and FFTW)

Wheels for Windows:

* are available for Python 3.8-3.13 (64 bit)
* are linked against OpenBLAS
* include the optional extension GLPK


Building and installing from source
========================================

.. rubric:: Required and optional software

The package requires version 3.x of Python, and building from
source requires core binaries and header files and libraries for Python.

The installation requires BLAS and LAPACK. Using an architecture
optimized implementation such as
`ATLAS <https://sourceforge.net/projects/math-atlas/>`_,
`OpenBLAS <http://www.openblas.net>`_, or
`MKL <https://software.intel.com/en-us/intel-mkl>`_ is recommended
and gives a large performance improvement over reference implementations
of the `BLAS <http://www.netlib.org/blas/>`_ and
`LAPACK <http://www.netlib.org/lapack/>`_ libraries.

The installation also requires SuiteSparse. We recommend linking against
a shared SuiteSparse library. It is also possible to build the required
components of SuiteSparse when building CVXOPT, but this requires the
SuiteSparse source which is no longer included with CVXOPT and must be
downloaded separately.

The following software libraries are optional.

* `The GNU Scientific Library GSL <www.gnu.org/software/gsl>`_.

* `FFTW <www.fftw.org>`_ is a C library for discrete Fourier transforms.

* `GLPK <www.gnu.org/software/glpk/glpk.html>`_ is a linear programming
  package.

* `MOSEK version 9 <www.mosek.com>`_ is a commercial library of convex
  optimization solvers.

* `DSDP5.8 <www-unix.mcs.anl.gov/DSDP>`_ is a semidefinite programming solver.


.. rubric:: Installation

CVXOPT can be installed globally (for all users on a UNIX/Linux system)
using the command::

    python setup.py install

It can also be installed locally (for a single user) using the command::

    python setup.py install --user

To test that the installation was successful, run the included tests using::

    python -m unittest discover -s tests

or alternatively, if `pytest` is installed::

    pytest

If Python does not issue an error message, the installation was successful.

It is also possible to install CVXOPT from source using pip::

    pip install cvxopt --no-binary cvxopt

Additional information can be found in the
`Python documentation <http://docs.python.org/install/index.html>`_.


Customizing the setup script
==================================

If needed, the default compilation can be customized by editing `setup.py` or
by means of environment variables. The following variables in the setup
script can be modified:

* ``BLAS_LIB_DIR``: the directory containing the LAPACK and BLAS libraries.

* ``BUILD_GSL``: set this variable to 1 if you would like to use the GSL
  random number generators for constructing random matrices in CVXOPT.
  If ``BULD_GSL`` is 0, the Python random number generators will be used
  instead.
* ``GSL_LIB_DIR``: the directory containing ``libgsl``.
* ``GSL_INC_DIR``: the directory containing the GSL header files.

* ``BUILD_FFTW``: set this variable to 1 to install the ``cvxopt.fftw`` module,
  which is an interface to FFTW.
* ``FFTW_LIB_DIR``: the directory containing ``libfftw3``.
* ``FFTW_INC_DIR``: the directory containing ``fftw.h``.

* ``BUILD_GLPK``: set this variable to 1 to enable support for the linear
  programming solver GLPK.
* ``GLPK_LIB_DIR``: the directory containing ``libglpk``.
* ``GLPK_INC_DIR``: the directory containing ``glpk.h``.

* ``BUILD_DSDP``: set this variable to 1 to enable support for the semidefinite
  programming solver DSDP.
* ``DSDP_LIB_DIR``: the directory containing ``libdsdp``.
* ``DSDP_INC_DIR``: the directory containing ``dsdp5.h``.

* ``SUITESPARSE_LIB_DIR``: the directory containing SuiteSparse libraries.
* ``SUITESPARSE_INC_DIR``: the directory containing SuiteSparse header files.
* ``SUITESPARSE_SRC_DIR``: the directory containing SuiteSparse source. The
  variables ``SUITESPARSE_LIB_DIR`` and ``SUITESPARSE_INC_DIR`` are ignored and
  relevant parts of SuiteSparse are build from source when
  ``SUITESPARSE_SRC_DIR`` is specified.

* ``MSVC``: set this variable to 1 if compiling with MSVC 14 or later

Each of the variables can be overridden by specifying an environment variable
with the prefix ``CVXOPT_``. For example, the following command installs CVXOPT
locally with ``BUILD_FFTW=1``::

     CVXOPT_BUILD_FFTW=1 python setup.py install --user

This approach also works with pip::

     export CVXOPT_BUILD_FFTW=1
     pip install cvxopt --no-binary cvxopt

Support for the linear, second-order cone, and quadratic programming
solvers in MOSEK is automatically enabled if both MOSEK and its
Python interface are installed.


Ubuntu/Debian
==================================


Building CVXOPT from source in Debian/Ubuntu requires the packages
``build-essential`` and ``python-dev`` as well as BLAS and LAPACK library packages
such as

* ``libopenblas-dev``
* ``libatlas-dev``
* ``libblas-dev`` and ``liblapack-dev``

If multiple BLAS and LAPACK libraries have been installed, you can verify
the current configuration using the following commands::

	  update-alternatives --config libblas.so.3
	  update-alternatives --config liblapack.so.3

.. seealso::

   Debian Science: `Handle different versions of BLAS and LAPACK
   <https://wiki.debian.org/DebianScience/LinearAlgebraLibraries>`_.

As of Ubuntu 16.04, SuiteSparse can be installed as a dynamic library by
installing the ``libsuitesparse-dev`` package. Alternatively, if SuiteSparse is
not available as a dynamic library, the
`SuiteSparse source <https://www.suitesparse.com>`_ must be available.

To build the optional CVXOPT extensions (DSDP, FFTW, GLPK, and GSL), the
following packages should be installed as well:

* ``libdsdp-dev``
* ``libfftw3-dev``
* ``libglpk-dev``
* ``libgsl-dev``

When all the necessary Ubuntu packages have been installed,
CVXOPT can be built with all extensions in Ubuntu 16.04 (or later) as follows:

.. code-block:: bash

    git clone https://github.com/cvxopt/cvxopt.git
    cd cvxopt
    git checkout `git describe --abbrev=0 --tags`
    export CVXOPT_BUILD_DSDP=1    # optional
    export CVXOPT_BUILD_FFTW=1    # optional
    export CVXOPT_BUILD_GLPK=1    # optional
    export CVXOPT_BUILD_GSL=1     # optional
    python setup.py install

To use the Intel MKL library instead of ATLAS or OpenBLAS, include the following commands
before running ``python setup.py install``:

.. code-block:: bash

    pip install mkl
    MKLLIB=mkl_rt
    PYDIR=`pip show mkl | grep Location | cut -d' ' -f 2`
    MKLDIR=`grep lib${MKLLIB} $PYDIR/mkl*/RECORD | cut -d, -f1`
    PREFIX_LIB=`dirname $PYDIR/$MKLDIR`
    export CVXOPT_LAPACK_LIB=${MKLLIB}
    export CVXOPT_BLAS_LIB=${MKLLIB}
    export CVXOPT_BLAS_LIB_DIR=${PREFIX_LIB}
    export CVXOPT_BLAS_EXTRA_LINK_ARGS="-L${PREFIX_LIB};-Wl,-rpath,${PREFIX_LIB};-l${MKLLIB}"

In older versions of Ubuntu where SuiteSparse is not available as a dynamic
library, the necessary SuiteSparse components can be built with CVXOPT
by downloading the SuiteSparse source and setting ``CVXOPT_SUITESPARSE_SRC_DIR``
to the SuiteSparse source directory:

.. code-block:: bash

    git clone https://github.com/DrTimothyAldenDavis/SuiteSparse.git
    pushd SuiteSparse
    git checkout v5.6.0
    popd
    export CVXOPT_SUITESPARSE_SRC_DIR=$(pwd)/SuiteSparse
    git clone https://github.com/cvxopt/cvxopt.git
    cd cvxopt
    git checkout `git describe --abbrev=0 --tags`
    export CVXOPT_BUILD_DSDP=1    # optional
    export CVXOPT_BUILD_FFTW=1    # optional
    export CVXOPT_BUILD_GLPK=1    # optional
    export CVXOPT_BUILD_GSL=1     # optional
    python setup.py install


macOS
=============

Building CVXOPT from source in macOS requires the Command-line tools which
can be installed using the command:

.. code-block:: bash

    xcode-select -p

.. rubric:: With Homebrew

`Homebrew <https://brew.sh>`_ users can build CVXOPT with FFTW, GLPK, and GSL
as follows:

.. code-block:: bash

    brew install gsl fftw suite-sparse glpk
    git clone https://github.com/cvxopt/cvxopt.git
    cd cvxopt
    git checkout `git describe --abbrev=0 --tags`
    export CVXOPT_BUILD_FFTW=1    # optional
    export CVXOPT_BUILD_GLPK=1    # optional
    export CVXOPT_BUILD_GSL=1     # optional
    python setup.py install

To use OpenBLAS instead of the built-in BLAS/LAPACK
libraries, include the following commands before running
``python setup.py install``:

.. code-block:: bash

    brew install openblas
    export CVXOPT_BLAS_LIB_DIR=/usr/local/opt/openblas/lib
    export CVXOPT_BLAS_LIB=openblas
    export CVXOPT_LAPACK_LIB=openblas

Alternatively, to use the Intel MKL library, include the following commands
before running ``python setup.py install``:

.. code-block:: bash

    pip install mkl
    MKLLIB=mkl_rt
    PYDIR=`pip show mkl | grep Location | cut -d' ' -f 2`
    MKLDIR=`grep lib${MKLLIB} $PYDIR/mkl*/RECORD | cut -d, -f1`
    PREFIX_LIB=`dirname $PYDIR/$MKLDIR`
    if [[ $OSTYPE == darwin* ]]; then
        install_name_tool -change @rpath/libiomp5.dylib @loader_path/libiomp5.dylib ${PREFIX_LIB}/libmkl_intel_thread.dylib
    fi
    export CVXOPT_LAPACK_LIB=${MKLLIB}
    export CVXOPT_BLAS_LIB=${MKLLIB}
    export CVXOPT_BLAS_LIB_DIR=${PREFIX_LIB}
    export CVXOPT_BLAS_EXTRA_LINK_ARGS="-L${PREFIX_LIB};-Wl,-rpath,${PREFIX_LIB};-l${MKLLIB}"
    pip install git+https://github.com/cvxopt/cvxopt


.. rubric:: Without Homebrew

If SuiteSparse is not available as a dynamic library, the necessary SuiteSparse
components can be built with CVXOPT by downloading the SuiteSparse source and
setting ``CVXOPT_SUITESPARSE_SRC_DIR`` to the SuiteSparse source directory:

.. code-block:: bash

    git clone https://github.com/DrTimothyAldenDavis/SuiteSparse.git
    pushd SuiteSparse
    git checkout v5.6.0
    popd
    export CVXOPT_SUITESPARSE_SRC_DIR=$(pwd)/SuiteSparse
    git clone https://github.com/cvxopt/cvxopt.git
    cd cvxopt
    git checkout `git describe --abbrev=0 --tags`
    python setup.py install


Windows
==============

We will assume that Python (64 bit), git, wget, and 7-zip
are installed and in the search path. These can be installed with the
`Chocolatey <https://chocolatey.org>`_ package manager::

    choco install -y wget git python2 7zip.commandline

We also will assume that the environment variable ``%PYTHON%`` contains
the path to the Python installation directory, e.g.,

.. code-block:: batch

    set PYTHON=c:\PythonXX

or alternatively,

.. code-block:: batch

    for /f %i in ('python -c "import sys, os; print(os.path.dirname(sys.executable))"') do set PYTHON=%i

where ``%`` must be replaced by ``%%`` if the above line is included in a batch file.

Finally, we will assume that pip is available;
if it is not, it can now be installed with ``easy_install``::

    %PYTHON%\Scripts\easy_install pip

.. rubric:: Python 3.5+

CVXOPT 1.2.0+ can be built for Windows (64 bit) with MSVC14 and OpenBLAS.

The following example shows how to build/install CVXOPT for x64:

.. code-block:: batch

    rem Download SuiteSparse source
    git clone https://github.com/DrTimothyAldenDavis/SuiteSparse.git
    cd SuiteSparse
    git checkout v5.8.1
    cd ..
    set CVXOPT_SUITESPARSE_SRC_DIR="%cd%\SuiteSparse"

    rem Download OpenBLAS
    wget https://github.com/xianyi/OpenBLAS/releases/download/v0.3.10/OpenBLAS-0.3.10-x64.zip
    wget https://raw.githubusercontent.com/xianyi/OpenBLAS/v0.3.10/LICENSE -O LICENSE_OpenBLAS-0.3.10
    mkdir OpenBLAS
    unzip OpenBLAS-0.3.10-x64.zip -d OpenBLAS
    set CVXOPT_BLAS_LIB_DIR="%cd%\OpenBLAS\lib" 
    set CVXOPT_BLAS_LIB=openblas
    set CVXOPT_LAPACK_LIB=openblas

    rem Clone CVXOPT repository, compile, install, and run tests
    git clone https://github.com/cvxopt/cvxopt.git
    cd cvxopt
    for /f %%a in ('git describe --abbrev^=0 --tags') do git checkout %%a
    set CVXOPT_MSVC=1
    python setup.py build --compiler=msvc
    python setup.py install
    python -m unittest discover -s tests
