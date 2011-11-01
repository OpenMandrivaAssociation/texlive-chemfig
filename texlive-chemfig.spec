Name:		texlive-chemfig
Version:	1.0a
Release:	1
Summary:	Draw molecules with easy syntax
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/chemfig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the command \chemfig{<code>}, which draws
2D molecules using the tikz package. The <code> contains
instructions for the drawing.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
