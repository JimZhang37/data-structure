class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == "":
        print("no user to look for")
        return False

    if not isinstance(group, Group):
        print(f'{group} is not a member of Group class')
        return False

    users = group.get_users()
    for i in users:
        if i == user:
            return True
    sub_groups = group.get_groups()
    for j in sub_groups:
        if is_user_in_group(user, j):
            return True
    return False

print(is_user_in_group(sub_child_user, parent)) # expect True
print(is_user_in_group("sub", parent))# expect False
print(is_user_in_group("sub", child))# expect False
print(is_user_in_group(sub_child_user, child))# expect True
print(is_user_in_group("sub", sub_child))# expect False
print(is_user_in_group(sub_child_user, sub_child))# expect True

#edge case 1
print(is_user_in_group("", sub_child))# expect False
group1 = "group1"
print(is_user_in_group(sub_child_user, group1))# expect False