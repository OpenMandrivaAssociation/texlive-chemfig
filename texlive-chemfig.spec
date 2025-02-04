Name:		texlive-chemfig
Version:	69227
Release:	1
Summary:	Draw molecules with easy syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/chemfig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the command \chemfig{<code>}, which draws
molecules using the tikz package. The <code> argument provides
instructions for the drawing operation. While the diagrams
produced are essentially 2-dimensional, the package supports
many of the conventional notations for illustrating the 3-
dimensional layout of a molecule. The package uses TikZ for its
actual drawing operations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/chemfig
%doc %{_texmfdistdir}/doc/generic/chemfig

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
