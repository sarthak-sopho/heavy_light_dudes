compilers = {
	"1": """
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential

CMD ["/bin/bash"]
	"""
}