%global packname  ape
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.0.7
Release:          2
Summary:          Analyses of Phylogenetics and Evolution
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ape_3.0-7.tar.gz
Requires:         R-gee R-nlme R-lattice
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-gee R-nlme R-lattice
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
ape provides functions for reading, writing, plotting, and manipulating
phylogenetic trees, analyses of comparative data in a phylogenetic
framework, analyses of diversification and macroevolution, computing
distances from allelic and nucleotide data, reading nucleotide sequences,
and several tools such as Mantel's test, computation of minimum spanning
tree, generalized skyline plots, estimation of absolute evolutionary rates
and clock-like trees using mean path lengths, non-parametric rate
smoothing and penalized likelihood. Phylogeny estimation can be done with
the NJ, BIONJ, ME, MVR, SDM, and triangle methods, and several methods
handling incomplete distance matrices (NJ*, BIONJ*, MVR*, and the
corresponding triangle method).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
