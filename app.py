import modal

stub = modal.Stub(name="modal-experiment")

@stub.function(
    mounts=[
        modal.Mount.from_local_dir("./public", remote_path="/assets")
    ]
)
@modal.web_server(port=8000, startup_timeout=60)
def run_server():
    return "python -m http.server 8000 --directory /assets"
