# revision 25103
# category Package
# catalog-ctan /macros/generic/chemfig
# catalog-date 2012-01-14 00:27:11 +0100
# catalog-license lppl1.3
# catalog-version 1.0e
Name:		texlive-chemfig
Version:	1.0e
Release:	1
Summary:	Draw molecules with easy syntax
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/chemfig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the command \chemfig{<code>}, which draws
2D molecules using the tikz package. The <code> contains
instructions for the drawing.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/chemfig/chemfig.sty
%{_texmfdistdir}/tex/generic/chemfig/chemfig.tex
%{_texmfdistdir}/tex/generic/chemfig/t-chemfig.tex
%doc %{_texmfdistdir}/doc/generic/chemfig/README
%doc %{_texmfdistdir}/doc/generic/chemfig/chemfig_doc_en.pdf
%doc %{_texmfdistdir}/doc/generic/chemfig/chemfig_doc_en.tex
%doc %{_texmfdistdir}/doc/generic/chemfig/chemfig_doc_fr.pdf
%doc %{_texmfdistdir}/doc/generic/chemfig/chemfig_doc_fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
