# Generated by generate_dockerfiles.py

FROM aorwall/swe-bench-sympy_sympy:latest

RUN git -c advice.detachedHead=false checkout ec9e3c0436fbff934fa84e22bf07f1b3ef5bfac3

RUN conda create -n sympy__sympy__1.1 python=3.9 mpmath flake8 -y

SHELL ["conda", "run", "-n", "sympy__sympy__1.1", "/bin/bash", "-c"]


RUN pip install mpmath==1.3.0 flake8-comprehensions

RUN pip install -e .


RUN git checkout ec9e3c0436fbff934fa84e22bf07f1b3ef5bfac3 .

ENV TESTBED_NAME=sympy__sympy__1.1

WORKDIR /home/swe-bench

COPY swebench_docker swebench_docker
COPY docker/entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]