from pathlib import Path
import shutil
from product_image_interface import ProductImageInterface  # Certifique-se de importar a interface

class LocalImageRepository(ProductImageInterface):

    def put_product_file(self, file_name, image) -> None:
        
        with open(file_name, "wb") as file:
            file.write(image.encode("utf-8"))

    def replace_product_file(self, file_name, image) -> None:
        
        if Path(file_name).exists():
            Path(file_name).unlink()
            self.put_product_file(file_name, image)

    def remove_product_file(self, file_name) -> None:
       
        if Path(file_name).exists():
            Path(file_name).unlink()

    def store_image_from_path(self, source_path, destination_path) -> None:
        
        dest_directory = Path(destination_path).parent
        dest_directory.mkdir(parents=True, exist_ok=True)

        
        shutil.copyfile(source_path, destination_path)

    def get_image_stream(self, image_path) -> bytes:
        
        with open(image_path, "rb") as file:
            return file.read()
