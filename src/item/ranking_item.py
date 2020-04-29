class RankingItem(object):
  id = 0
  rank = 0
  image_link = None
  link = None
  headline = None
  lede = None
  office = None
  view = 0
  previous_item = None

  def to_dict(self):
    return {
      'id': self.id,
      'rank': self.rank,
      'image_link': self.image_link,
      'link': self.link,
      'headline': self.headline,
      'lede': self.lede,
      'office': self.office,
      'view': self.view,
      'previous_item': {} if self.previous_item is None else self.previous_item.to_dict()
    }
  
  @staticmethod
  def from_dict(dictObj):
    item = RankingItem()
    item.id = dictObj['id']
    item.rank = dictObj['rank']
    item.image_link = dictObj['image_link']
    item.link = dictObj['link']
    item.headline = dictObj['headline']
    item.lede = dictObj['lede']
    item.office = dictObj['office']
    item.view = dictObj['view']
    item.previous_item = None if dictObj['previous_item'] == {} else RankingItem.from_dict(dictObj['previous_item'])
    return item

  def print_item(self):
    print('======================== print_item ========================')
    print(f'    id: {self.id}')
    print(f'    rank: {self.rank}')
    print(f'    image_link: {self.image_link}')
    print(f'    link: {self.link}')
    print(f'    headline: {self.headline}')
    print(f'    lede: {self.lede}')
    print(f'    office: {self.office}')
    print(f'    view: {self.view}')
