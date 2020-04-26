class RankingItem:
    num = 0
    link = ""
    headline = ""
    lede = ""
    office = ""
    view = 0

    def printItem(self):
        print('======================== printItem ========================')
        print(f'    num: {self.num}')
        print(f'    link: {self.link}')
        print(f'    headline: {self.headline}')
        print(f'    lede: {self.lede}')
        print(f'    office: {self.office}')
        print(f'    view: {self.view}')
