class Dictionary:
    def __init__(self, name, json_path):
        self.name = name
        self.hierarchy = self._load_dictionary(json_path)
    
    def _load_dictionary(self, json_path):        
        import json
        with open(json_path, encoding='utf-8') as f:
            dictionary = json.load(f)
        return dictionary
    
    def show_hierarchy(self, nested=None, depth=0):
        from collections import abc
        if nested == None:
            nested = self.hierarchy
        for key, value in nested.items():
            print('{}|--{}'.format('   '*depth, key))
            if isinstance(value, abc.Mapping):
                self.show_hierarchy(value,depth+1)
    
    def get_words(self, categories=None):
        wordset = set()
        root = self.hierarchy
        if categories:
            if type(categories) == str:
                categories = [categories]
            for category in categories:
                root = root.get(category, {})
        if not isinstance(root, dict):
            return set(root)
        for _, words in self._nested_dict_iter(root):
            wordset.update(words)
        return wordset
    
    def _nested_dict_iter(self, nested):
        from collections import abc
        for key, value in nested.items():
            if isinstance(value, abc.Mapping):
                yield from self._nested_dict_iter(value)
            else:
                yield key, value
    
    def find_categories(self, word):
        categories = set()
        for key, words in self._nested_dict_iter(self.hierarchy):
            if word in words:
                categories.add(key)
        return categories
    
    def __str__(self):
        return 'Dictionary:{}'.format(self.name)
