# revision 23913
# category Package
# catalog-ctan /graphics/pgf/contrib/circuitikz
# catalog-date 2009-11-25 18:21:28 +0100
# catalog-license lppl
# catalog-version 0.2.3
Name:		texlive-circuitikz
Version:	0.2.3
Release:	1
Summary:	Draw electrical networks with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/circuitikz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros for naturally typesetting
electrical and (somewhat less naturally, perhaps) electronic
networks. It is designed as a tool that is easy to use, with a
lean syntax, native to LaTeX, and directly supporting PDF
output format. So is based on the very impressive pgf/TikZ
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/circuitikz/circuitikz.code.tex
%{_texmfdistdir}/tex/latex/circuitikz/circuitikz.sty
%{_texmfdistdir}/tex/latex/circuitikz/circuitikz1.code.tex
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircbipoles.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcirccurrent.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcirclabel.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircmath.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircmonopoles.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircquadpoles.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircshapes.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcirctripoles.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircutils.sty
%{_texmfdistdir}/tex/latex/circuitikz/pgfcircvoltage.sty
%{_texmfdistdir}/tex/latex/circuitikz/t-circuitikz.tex
%doc %{_texmfdistdir}/doc/latex/circuitikz/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/circuitikz/README
%doc %{_texmfdistdir}/doc/latex/circuitikz/circuitikz-context.pdf
%doc %{_texmfdistdir}/doc/latex/circuitikz/circuitikz-context.tex
%doc %{_texmfdistdir}/doc/latex/circuitikz/circuitikzmanual.pdf
%doc %{_texmfdistdir}/doc/latex/circuitikz/circuitikzmanual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
