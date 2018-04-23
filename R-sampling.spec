#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sampling
Version  : 2.8
Release  : 4
URL      : https://cran.r-project.org/src/contrib/sampling_2.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sampling_2.8.tar.gz
Summary  : Survey Sampling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sampling-lib
Requires: R-lpSolve
BuildRequires : R-lpSolve
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-sampling package.
Group: Libraries

%description lib
lib components for the R-sampling package.


%prep
%setup -q -c -n sampling

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521170901

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521170901
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sampling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sampling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sampling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sampling|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sampling/DESCRIPTION
/usr/lib64/R/library/sampling/INDEX
/usr/lib64/R/library/sampling/Meta/Rd.rds
/usr/lib64/R/library/sampling/Meta/data.rds
/usr/lib64/R/library/sampling/Meta/features.rds
/usr/lib64/R/library/sampling/Meta/hsearch.rds
/usr/lib64/R/library/sampling/Meta/links.rds
/usr/lib64/R/library/sampling/Meta/nsInfo.rds
/usr/lib64/R/library/sampling/Meta/package.rds
/usr/lib64/R/library/sampling/Meta/vignette.rds
/usr/lib64/R/library/sampling/NAMESPACE
/usr/lib64/R/library/sampling/R/sampling
/usr/lib64/R/library/sampling/R/sampling.rdb
/usr/lib64/R/library/sampling/R/sampling.rdx
/usr/lib64/R/library/sampling/data/MU284.rda
/usr/lib64/R/library/sampling/data/belgianmunicipalities.rda
/usr/lib64/R/library/sampling/data/swissmunicipalities.rda
/usr/lib64/R/library/sampling/doc/HT_Hajek_estimators.R
/usr/lib64/R/library/sampling/doc/HT_Hajek_estimators.Snw
/usr/lib64/R/library/sampling/doc/HT_Hajek_estimators.pdf
/usr/lib64/R/library/sampling/doc/UPexamples.R
/usr/lib64/R/library/sampling/doc/UPexamples.Snw
/usr/lib64/R/library/sampling/doc/UPexamples.pdf
/usr/lib64/R/library/sampling/doc/calibration.R
/usr/lib64/R/library/sampling/doc/calibration.Snw
/usr/lib64/R/library/sampling/doc/calibration.pdf
/usr/lib64/R/library/sampling/doc/index.html
/usr/lib64/R/library/sampling/help/AnIndex
/usr/lib64/R/library/sampling/help/aliases.rds
/usr/lib64/R/library/sampling/help/paths.rds
/usr/lib64/R/library/sampling/help/sampling.rdb
/usr/lib64/R/library/sampling/help/sampling.rdx
/usr/lib64/R/library/sampling/html/00Index.html
/usr/lib64/R/library/sampling/html/R.css
/usr/lib64/R/library/sampling/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sampling/libs/sampling.so
/usr/lib64/R/library/sampling/libs/sampling.so.avx2
/usr/lib64/R/library/sampling/libs/sampling.so.avx512
