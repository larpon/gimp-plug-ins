gimp-plug-ins
=============
###a collection of GIMP plug-ins.
As of now only one plug-in is ready - but it's pretty neat!

## Layer export
This plug-in will export your document's layers to the format specified in the *File pattern* field.
You can export the layers based on their visibility by toggling the *Visibility* drop-down.
In the *Token* drop-down you can choose what the *#* token in the *File pattern* field should be substituted with:
* `# = Layer name` will replace *#* with the layer name.
* `# = Count` will replace *#* with an increasing number for each layer.
* `# = Count (zero padded)` will replace *#* with an increasing number for each layer with zero padding - eg. `0001.png`.

Happy exporting!

| Screenshots|  |
| ------------- | ------------- |
| ![Screenshot](./screenshot_2.png)  | ![Screenshot](./screenshot_1.png)  |
| Puts itself into the *file* dialog  | The dialog for export options |
